document.querySelectorAll(".close").forEach(function (element) {
  element.addEventListener("click", function () {
    this.parentElement.style.display = "none";
  });
});
