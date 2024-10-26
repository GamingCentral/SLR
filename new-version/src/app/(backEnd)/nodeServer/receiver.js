import express from 'express';
const app=express();
const bodyParser = require('body-parser');

app.use(bodyParser.json())
app.post('/receiver',(req,res)=>{
    const data = req.body;
    console.log("Recieved data: ",data);
    res.status(200).send("Data Recieved");
});

const Port = 3000;
app.listen(Port,()=>{
    console.log('node running on port 3000');
})
