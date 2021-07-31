import { Typography, Grid, Paper, TextField } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: "20px",
    margin: "20px",
    textAlign: "center",
    border: "1px solid #80190E",
    borderRadius: "10px",
  },
  title: {

  },
  author: {

  },
  abstract: {

  },
  terms: {

  },
  label: {

  }
}));

export default function Doc(props) {
  const classes = useStyles();
  return (
    <Grid container className={classes.root}>
      <Grid item xs={12}>
        <Paper className={classes.paper} elevation={20}>
          <Typography className={classes.label} variant="h6">
            Titulo: 
          </Typography> 
          <Typography variant="body1" className={classes.title}>
            {props.doc.Title}
          </Typography>
          <Typography className={classes.label} variant="h6">
            Autor: 
          </Typography> 
          <Typography variant="body1" className={classes.author}>
            {props.doc.Author} 
          </Typography>
          <Typography className={classes.label} variant="h6">
            Resumen: 
          </Typography> 
          <Typography variant="body1" className={classes.abstract}>
            {props.doc.Abstract}
          </Typography>
          <Typography className={classes.label} variant="h6">
          Términos Relacionados: 
          </Typography> 
          <Typography variant="body1" className={classes.terms}>
           {props.doc.Terms}
          </Typography>
          <Typography className={classes.label} variant="h6">
          Doc ID: 
          </Typography> 
          <Typography variant="body1" className={classes.terms}>
           {props.doc.ID}
          </Typography>
        </Paper>
      </Grid>
    </Grid>
  );
}
