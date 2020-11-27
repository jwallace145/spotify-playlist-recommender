import React from 'react';
import { Button } from './Button';
import './SongIntake.css';

function SongIntake() {
  return (
    <div className='hero-container'>
      <video src="/videos/video-2.mp4" autoPlay loop muted />
      <h1>Music Artificial Intelligence</h1>
      <p>What are you waiting for?</p>
      <div className="hero-btns">
        <Button className='btns' buttonStyle='btn--outline' buttonSize='btn--large'> Get Started </Button>
      </div>
    </div>
  )
}

export default SongIntake;
