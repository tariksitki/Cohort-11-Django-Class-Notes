
let message = document.querySelector(".message");

// setTimeout(function () {
//     message.style.display = "none"
// }, 3000);


setTimeout(() => (message.style.display = "none"), 3000);

// Not:  settime icinde arrow func kullanirken {} kullanmiyoruz. 