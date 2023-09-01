import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './LoginForm.css';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  
<<<<<<< HEAD
  const apiUrl = `http://localhost:5001/A2/login`;
  // const apiUrl = `https://cntr2-ietsvmyfaq-nn.a.run.app/A2/login`;
=======
  // const apiUrl = `http://localhost:5001/A2/login`;
  const apiUrl = `https://cntr2-ietsvmyfaq-uc.a.run.app/A2/login`; // container 2 URL
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
  const handleLogin = (event) => {
    event.preventDefault();
    (async () => {
    const loginData = {
      "Email" : email,
      "Password" : password
    };

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      });
  
      if (response.ok) {
        // Login successful, handle the response accordingly
        console.log('Login successful!');
        alert('Login successful!');
        // navigate('/sessionData/'+email);
<<<<<<< HEAD
        navigate(`/sessionData?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`);
=======
        navigate(`/sessionData/${email}`); //naviagte to the sessionData page
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7

        // navigate('/sessionData', { state: { email } });
      } else {
        // Login failed, handle the error response
        console.error('Login failed. Invalid credentials');
        alert('Login failed. Invalid credentials!');
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
    }
  
    // Clear the form fields after login
    setEmail('');
    setPassword('');
  })();
};

  return (
    <div className="login-form">
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <div className="form-field">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
          />
        </div>
        <div className="form-field">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
          />
        </div>
        <div className="form-field">
          <button type="submit">Login</button>
        </div>
        <div className="form-field">
          <Link to="/RegistrationForm">Haven't registered yet? Register</Link>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
