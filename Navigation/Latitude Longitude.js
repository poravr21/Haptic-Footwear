const express = require('express');
const https = require('https');
const app = express();
const prompt = require('prompt-sync')();
const fetch = require('node-fetch');
const ENDPOINT = "https://maps.googleapis.com/maps/api/directions/json?";
const API_KEY = "AIzaSyDAZeBi8-k5Mbk627eyM7HVHLV0gTEGuME";
const origin = prompt("enter origin");
const destination = prompt("enter destination");
const ORIGIN = origin.replace(/\s/g, "+");
const DESTINATION = destination.replace(/\s/g, "+");
const URL = ENDPOINT + "origin=" + ORIGIN + "&destination=" + DESTINATION + "&key=" + API_KEY;
console.log(URL);
async function getData(){
    const response = await fetch(URL);
    const data = await response.json();
    console.log("the lats and longs of the turning points are: ");
    for( x in data.routes[0].legs[0].steps){
        console.log(data.routes[0].legs[0].steps[x].start_location.lat + " " + data.routes[0].legs[0].steps[x].start_location.lng);
    }
    let x1=prompt("Enter latitude:");
    let y1=prompt("Enter longitude:");
    let eps=0.00001;
    for( x in data.routes[0].legs[0].steps)
    {
        let x0=data.routes[0].legs[0].steps[x].start_location.lat;
        let y0=data.routes[0].legs[0].steps[x].start_location.lng;
        if((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1) < eps)
        {
            console.log(data.routes[0].legs[0].steps[x].html_instructions);
        }
    }
}
getData();
// const DATA = JSON.parse(data[0]);
// console.log(DATA);
// console.log(DIRECTIONS);