const userAction = async () => {
  const response = await fetch('http://kimsufi2.jaguenaud.org:25146/portefolio/luis/get_poemes/');
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
  console.log(myJson);
}

userAction()

const modal = document.getElementById("loginModal");

// Get the button that opens the modal
const joinBtn = document.getElementById("joinButton");
const logInBtn = document.getElementById("logInButton");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
joinBtn.onclick = function() {
  modal.style.display = "block";
}

const userField = document.getElementById("pwdField");
const pwdField = document.getElementById("pwdField");
const txtField = document.getElementById("textArea");

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

a = function() {
    console.log("Test");
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

logInBtn.onclick = function(e) {
    console.log(txtField.value.replaceAll("\n","-enter-").replaceAll(" ", "-space-").replaceAll(".", "").replaceAll(",", ""));
}

pwdField.onkeypress = function(e){
    if (!e) e = window.event;
    var keyCode = e.code || e.key;
    if (keyCode == 'Enter'){
        // Enter pressed
        a()
        return false;
    }
}

