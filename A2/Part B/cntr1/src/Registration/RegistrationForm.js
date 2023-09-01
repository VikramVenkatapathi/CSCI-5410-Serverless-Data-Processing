import React, { useState } from 'react';
import { useNavigate, Link  } from 'react-router-dom';

import './RegistrationForm.css';

const RegistrationForm = () => {
  const [Name, setName] = useState('');
  const [Password, setPassword] = useState('');
  const [Email, setEmail] = useState('');
  const [Location, setLocation] = useState('');
  const navigate = useNavigate();

  const apiUrl = `http://localhost:5000/A2/register`;
  
<<<<<<< HEAD
  // const apiUrl = `https://cntr1-ietsvmyfaq-nn.a.run.app/A2/register`;
=======
  const apiUrl = `https://cntr1-ietsvmyfaq-uc.a.run.app/A2/register`; //container1 URL
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7

  const handleRegistration = async (event) => {
    event.preventDefault();

    const registrationData = {
      "Name": Name,
      "Password" : Password,
      "Email" : Email,
      "Location" : Location,
    };

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(registrationData),
      });

      if (response.ok) {
        // Registration successful, handle the response accordingly
        console.log('Registration successful!');
        setName('');
        setPassword('');
        setEmail('');
        setLocation('');
        // setRegistrationStatus('success');
        alert('Registration successful!');
        navigate('/login'); // Redirect to the login page
      }
      else if (response.status === 409) {
        // Email already exists, handle the response
        console.error('Email already exists.');
        alert('Email already exists. Please choose a different email.');
      }  
      else {
        // Registration failed, handle the error response
        console.error('Registration failed.');
        // setRegistrationStatus('error');
        alert('Registration failed. Please try again.');
      }
    } catch (error) {
      console.error('Error occurred during registration:', error);
    //   setRegistrationStatus('error');
    alert('Error occurred during registration. Please try again.');
    }
    
  };

  return (
    <div className="registration-form">
      <h1>Registration Form</h1>
      <form onSubmit={handleRegistration}>
        <div className="form-field">
          <label htmlFor="name">Name:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <input
            type="text"
            id="name"
            value={Name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Enter your name"
          />
        </div>
        <div className="form-field">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={Password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
          />
        </div>
        <div className="form-field">
          <label htmlFor="email">Email:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <input
            type="email"
            id="email"
            value={Email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
          />
        </div>
        <div className="form-field">
          <label htmlFor="location">Location:</label>&nbsp;
          <input
            type="text"
            id="location"
            value={Location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Enter your location"
          />
        </div>
        <div className="form-field center">
          <button type="submit"><b>Register</b></button>
        </div>
        <div className="form-field">
  <Link to="/login">Already registered? Login</Link>
</div>
      </form>

    </div>
  );
};

export default RegistrationForm;
