var mqtt;
var reconnectTimeout = 100;
var host = "whale.hacking-lab.com";
var port = 9001;
var useTLS = false;
var username = "workshop";
var password = "2fXc7AWINBXyruvKLiX";
var clientid = localStorage.getItem("clientid");
if (clientid == null) {
  clientid = ("" + Math.round(Math.random() * 1000000000000000)).padStart(
    16,
    "0"
  );
  localStorage.setItem("clientid", clientid);
}
var topic = "HV19/gifts/" + clientid;
// var topic = 'HV19/gifts/'+clientid+'/flag-tbd';
var cleansession = true;
