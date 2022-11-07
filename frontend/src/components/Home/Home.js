import React, { useState, useEffect } from "react";
import {
  Grid,
  Paper,
  Button,
  Typography,
  TableContainer,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  TextField,
} from "@mui/material";
import { useForm } from "react-hook-form";
import "./Home.css";

const Home = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();

  const [data, setData] = useState([{}]);

  const urlPattern =
    /[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&//=]*)?/gi;

  const fetchData = async () => {
    const response = await fetch("http://127.0.0.1:8000/");
    const data = await response.json();
    setData(data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const onSubmit = (data) => {
    var formData = new FormData();
    formData.append("original_url", data.url);
    fetch("http://127.0.0.1:8000/add/", {
      method: "POST",
      headers: {
        Accept: "*/*",
      },
      body: formData,
    })
      .then((res) => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res.json();
      })
      .then((data) => {
        fetchData();
        reset();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <Paper sx={{ p: 10, minHeight: "100vh" }}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Typography variant="h4">Shortened URL</Typography>
        </Grid>
        <Grid item xs={12}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <TextField
              required
              id="url"
              name="url"
              placeholder="Type a url to shorten"
              {...register("url", { required: true, pattern: urlPattern })}
              error={errors.url ? true : false}
              className="input"
            />
            <Button
              variant="contained"
              size="large"
              sx={{ pb: 1.4, pt: 2 }}
              type="submit"
            >
              Submit
            </Button>
          </form>
        </Grid>
      </Grid>
      <Grid item xs={12} sx={{ mt: 10 }}>
        <Typography variant="h4">URL Shortener</Typography>
        <TableContainer component={Paper} sx={{ width: "50%" }}>
          <Table sx={{ minWidth: 350 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>
                  <b>Original URL</b>
                </TableCell>
                <TableCell align="right">
                  <b>Shortened Url</b>
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {data.map((data) => (
                <TableRow
                  key={data.id}
                  sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {data.original_url}
                  </TableCell>
                  <TableCell align="right">
                    <a href={data.shortened_url}>{data.shortened_url}</a>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Grid>
    </Paper>
  );
};

export default Home;
