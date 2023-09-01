import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import './SessionData.css';

const SessionData = () => {
  const [userData, setUserData] = useState(null);
  const { email } = useParams();
  const { password } = useParams();
  const navigate = useNavigate();
  const [onlineUsers, setOnlineUsers] = useState([]);

  
  const cntr3URL = `http://localhost:5002`;

<<<<<<< HEAD
  // const cntr3URL = `https://cntr3-ietsvmyfaq-nn.a.run.app`
  // const apiUrl = `${cntr3URL}/A2/sessionData/email=${email}&password=${password}`
  const apiUrl = `${cntr3URL}/A2/sessionData?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
  //email=<email>&password=<password>
=======
  const cntr3URL = `https://cntr3-ietsvmyfaq-uc.a.run.app` //conatiner3 URL
  const apiUrl = `${cntr3URL}/A2/sessionData/${email}`
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
  
  // const apiUrl = `https://cntr3-ietsvmyfaq-uc.a.run.app/A2/sessionData/${email}`;
  const usersOnlineUrl = `${cntr3URL}/A2/sessionData/usersOnline/${email}`; 
  // const usersOnlineUrl = `http://localhost:5002/A2/sessionData/usersOnline/${email}`;
  
  const [showPassword, setShowPassword] = useState(false); // State for password visibility



  const togglePasswordVisibility = () => {
    setShowPassword((prevShowPassword) => !prevShowPassword);
  };

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch(apiUrl);
        const jsonData = await response.json();
        setUserData(jsonData);
      } catch (error) {
        console.log('Error fetching user data:', error);
      }
    };

    const fetchOnlineUsers = async () => {
      try {
        const response = await fetch(usersOnlineUrl);
        const jsonData = await response.json();
        setOnlineUsers(jsonData);
      } catch (error) {
        console.log('Error fetching online users:', error);
      }
    };


    fetchUserData();
    fetchOnlineUsers();
  }, [apiUrl, usersOnlineUrl]);


  const handleLogoutRequest = async () => {
    try {
      // const apiUrl = `http://localhost:5002/A2/sessionData/${email}/logout`;
      const apiUrl = `${cntr3URL}/A2/sessionData/${email}/logout`;
      
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      if (response.ok) {
        // Logout successful
        console.log('Logout successful!');
        alert('Logout successful!');
        navigate('/login'); //Redirect to login page
        // handleLogout(); // Call the logout handler from props
      } else {
        // Logout failed, handle the error response
        console.error('Logout failed.');
        alert('Logout failed!');
      }
    } catch (error) {
      console.error('Error occurred during logout:', error);
    }
  };

  return (
    <div className="session-data-container">
      <h1>Hi, {email} you are logged in. </h1>
      <h2>Your Session data</h2>
      {userData ? (
        <div>
          <form className="user-form">
            <div className="form-group">
              <label htmlFor="name">Name:</label>
              <input type="text" id="name" value={userData.Name} readOnly />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email:</label>
              <input type="email" id="email" value={userData.Email} readOnly />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password:</label>
              <input
                type={showPassword ? 'text' : 'password'}
                id="password"
                value={userData.Password}
                readOnly={!showPassword}
                onBlur={togglePasswordVisibility}
                onFocus={togglePasswordVisibility}
              />
            </div>
            <div className="form-group">
              <label htmlFor="location">Location:</label>
              <input type="text" id="location" value={userData.Location} readOnly />
            </div>
            <div className="form-group">
              <label htmlFor="online">Online:</label>
              <input type="text" id="online" value={userData.Online} readOnly />
            </div>
            <div className="form-group">
              <label htmlFor="offline">Offline:</label>
              <input type="text" id="offline" value={userData.Offline} readOnly />
            </div>
            <div className="form-group">
              <label htmlFor="timestamp">Timestamp:(last login)</label>
              <input type="text" id="timestamp" value={userData.Timestamp} readOnly />
            </div>
          </form>
          <button className="logout-button" onClick={handleLogoutRequest}>
            Logout
          </button>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
       <h2>Here	are	other	users	who	are	online</h2>
      {onlineUsers.length > 0 ? (
        <ul>
          {onlineUsers.map((userId) => (
            // <li key={user.Email}>{user.Name}</li>
            <li key={userId}>{userId}</li>
          ))}
        </ul>
    
      ) : (
        <p>No users are currently online.</p>
      )}
    </div>
  );
  
};

export default SessionData;