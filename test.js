// ==UserScript==
// @name        Patreon bulk attachment downloader
// @author      anadius
// @namespace   anadius.su
// @match       https://www.patreon.com/posts/*
// @version     1.0.2
// @grant       none
// @require     https://cdn.jsdelivr.net/npm/jszip@3.10.0/dist/jszip.min.js
// @require     https://cdn.jsdelivr.net/npm/filesaver.js@1.3.4/FileSaver.min.js
// @run-at      document-end
// ==/UserScript==

window.addEventListener("load", () => {

const ATTACHMENTS = document.querySelector("[data-tag=post-attachments]");
const DOWNLOAD_BUTTON = document.createElement("button");
const TITLE = document.querySelector("[data-tag=post-title]").textContent;

const makeCheckbox = (attachment) => {
  const cb = document.createElement("input");
  cb.type = "checkbox";
  if(attachment !== null) {
    cb.filename = attachment.textContent;
    cb.url = attachment.href;
    cb.style.height = "1.35rem";
    cb.classList.add("attachment");
  }
  return cb;
};

const getCheckboxes = () => ATTACHMENTS.querySelectorAll("input.attachment[type=checkbox]");

const readAsBinaryString = blob => new Promise(resolve => {
  const reader = new FileReader();
  reader.onload = function(event) {
    resolve(event.target.result);
  };
  reader.readAsBinaryString(blob);
});

const download = async e => {
  e.preventDefault();

  const zip = new JSZip();
  DOWNLOAD_BUTTON.disabled = "disabled";

  for(const cb of getCheckboxes()) {
    if(cb.checked) {
      const response = await fetch(cb.url);
      const blob = await response.blob();
      cb.classList.add("downloaded");
      zip.file(cb.filename, await readAsBinaryString(blob), {binary: true});
    }
  }

  zip.generateAsync({type:"blob"})
    .then(function(content) {
    saveAs(content, `${TITLE}.zip`);
  });
  DOWNLOAD_BUTTON.disabled = "";
};


for(const attachment of ATTACHMENTS.querySelectorAll("[data-tag=post-attachment-link]")) {
  attachment.before(makeCheckbox(attachment));
}

const div = document.createElement("div");
const toggleAll = makeCheckbox(null);
toggleAll.addEventListener("click", () => {
  for(const cb of getCheckboxes()) {
    cb.checked = toggleAll.checked;
  }
});

DOWNLOAD_BUTTON.innerHTML = "Download";
DOWNLOAD_BUTTON.addEventListener("click", download);

const label = document.createElement("label");
label.innerHTML = " Toggle all ";
label.prepend(toggleAll);

div.append(label, DOWNLOAD_BUTTON);
ATTACHMENTS.append(div);

document.styleSheets[0].addRule("input.attachment.downloaded[type=checkbox] + a:after",'content: "✅"');

})();