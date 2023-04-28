import { useState } from "react";
import ResultDisplay from "./components/ResultDisplay";
import './App.css';

import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function App() {
  const [model_names, setModel_names] = useState([
    { name: "Bert Model", pred: 0 },
    { name: "BERT DistilBERT MetaDistil", pred: 0 },
    { name: "BERT + BERT DistilBERT MetaDistil", pred: 0 }
  ]);
  const [text, setText] = useState([''])

  const valueHandler = event => {
    setText(event.target.value);
  }

  const get_senti_preds = () => {
    console.log("Request Sent!!!");
    fetch('/sentiment_prediction', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: text
      })
    }).then(
      res => res.json()
    ).then(
      res => {
        console.log(res.predictions);
        setModel_names([
          { name: "Bert Model", pred: res.predictions[0] },
          { name: "BERT DistilBERT MetaDistil", pred: res.predictions[1] },
          { name: "BERT + BERT DistilBERT MetaDistil", pred: res.predictions[2] }
        ])
        console.log("Recived Responses!!!");
      }
    );
  }

  return (
    <div className="App">
      <h1>Improving MetaDistil Framework Demo</h1>
      <div className='title'>
        <TextField
          label="Entert Text"
          onChange={valueHandler}
          value={text}
        />
        <Button variant="contained" size="large" onClick={get_senti_preds}>
          Predict Sentiment
        </Button>
      </div>

      <ResultDisplay model_names={model_names} />
    </div>
  );
}

export default App;
