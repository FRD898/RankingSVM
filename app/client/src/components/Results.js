import Doc from "./Doc";
import { TextField, IconButton } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { useEffect, useState } from "react";
import axios from "axios";
import SearchIcon from '@material-ui/icons/Search';


const useStyles = makeStyles((theme) => ({
  root: {
    //backgroundColor: "blue",
    padding: "40px",
  }
}));

export default function ResultsPanel() {
  const [docList, setDocList] = useState([{
    Abstract: " ",
    Author: " ",
    ID: " ",
    "Publication Type": " ",
    Source: " ",
    Terms:
      " ",
    Title: " ",
    UI: " ",
    date: " "
  }]);
  const classes = useStyles();
  const [noResult, setNoResult] = useState(true);
  const [query, setQuery] = useState("")

  function handleSearch(e){
    e.preventDefault()
    axios.get('http://127.0.0.1:4000/search', {
      params: {
        query: query
      }
    }).then((response)=>{
      console.log(response)
      if(response.status===200){
        setDocList(response.data.docs)
        setNoResult(false)
      }else{
        setNoResult(true);
      }
    }).catch((error)=>{
      console.error(error)
    })    
  }

  const ListofDocs = docList.map((item, index) => {
    return <Doc doc={item} key={index} />;
  });
  return (
    <div className={classes.root}>
      <div >
        <TextField id="outlined-basic" label="Buscar..." variant="outlined" onChange={(e)=>setQuery(e.target.value)} />
        <IconButton onClick={handleSearch}><SearchIcon></SearchIcon></IconButton>
      </div>
      {noResult?<div>No se encontraron documentos</div>:<ul>{ListofDocs}</ul>}
    </div>)
}
