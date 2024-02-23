const express = require('express')
const axios = require('axios')
const app = express()
const keyz = require("key.js").keystuff()
// tail = "N523AE"

const AIRCRAFT_API_KEY = keyz;
const AIRCRAFT_API_HOST = "aerodatabox.p.rapidapi.com";

app.get('/', async(req,res) => {

    const tail = req.query.tail;
    if (!tail) {
        return res.status(400).send('Tail number is required');
    }
    try {
         pullNewAircraft(tail, (returns) =>{
            if (returns) {
                res.json(returns);
            } else {
                console.log(returns);
                // res.send("fuck you")
                res.status(404).send("Aircraft Bad");
            }
         });
       
    } catch (error) {
        console.error(error);
        res.status(500).send('Serr bad');
    }
})



async function pullNewAircraft(tail,returns){
    const options = {
        method: 'GET',
        url: `https://${AIRCRAFT_API_HOST}/aircrafts/${tail}`,
        // url: 'https://aerodatabox.p.rapidapi.com/aircrafts/%7BsearchBy%7D/VP-BZP',

        headers: {
          'X-RapidAPI-Key': AIRCRAFT_API_KEY,
          'X-RapidAPI-Host': AIRCRAFT_API_HOST
        }
      };
      try {
          const response = await axios.request(options).then((data) => {
            returns(data.data);
            console.log(response.data)
          });
      } catch (error) {
        console.error(error);
          returns(null);
      }
}



app.listen(8080)