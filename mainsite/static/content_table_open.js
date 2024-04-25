const popupOverlay = document.querySelector('.popup-overlay');
const popup = document.querySelector('.popup');

function showPopup() {
  popupOverlay.style.display = "block";
}
 
function hidePopup() {
  popupOverlay.style.display = "none";
}
 
popupOverlay.addEventListener("click", hidePopup);
popup.addEventListener("click", (event) =&gt; event.stopPropagation());