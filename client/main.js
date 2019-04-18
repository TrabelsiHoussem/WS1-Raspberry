function led(etat) {
    //alert(etat);



    if (etat == 'undefined') {
        return;
    }
    //here is to create the object that can send data to the raspberry pi
    //from your raspberry
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "http://192.168.1.4:8089", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("etat=" + etat);

}
