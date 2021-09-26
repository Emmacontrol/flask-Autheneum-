require('dotenv').config()
const express = require('express')
const app = express()
const port = 3000
const output = `Hello.  MYENVVAR is ${process.env.MYENVVAR}`
app.get('/', (req, res) => res.send(output))
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
