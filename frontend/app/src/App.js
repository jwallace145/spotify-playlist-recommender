import React from 'react';
import './App.css';

class SongIntake extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      title: '',
      artist: '',
      album: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
    fetch("http://127.0.0.1:5000/insert-song", {
      method: "POST",
      body: JSON.stringify({
        title: this.state.title,
        artist: this.state.artist,
        album: this.state.album
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
      .then(response => response.json())
      .then(json => console.log(json));
  }

  handleClick(event) {

  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>Title</label>
          <input type="text" name="title" onChange={this.handleChange} />
        </div>
        <div>
          <label>Album</label>
          <input type="text" name="album" onChange={this.handleChange} />
        </div>
        <div>
          <label>Artist</label>
          <input type="text" name="artist" onChange={this.handleChange} />
        </div>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default SongIntake;
