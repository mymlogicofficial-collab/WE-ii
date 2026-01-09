import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import ChatInterface from './ChatInterface';
import '../App.css';

function ChatApp() {
  const { isLoading, isAuthenticated, loginWithRedirect, logout, user } = useAuth0();

  if (isLoading) {
    return (
      <div className="app-container">
        <header className="app-header">
          <div className="header-content">
            <h1 className="app-title">WE-ii Chat</h1>
          </div>
        </header>
        <div className="loading-screen">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return (
      <div className="app-container">
        <header className="app-header">
          <div className="header-content">
            <h1 className="app-title">WE-ii Chat</h1>
          </div>
        </header>
        <div className="welcome-screen">
          <h1>Welcome to WE-ii Chat</h1>
          <p>
            Secure chat interface powered by Auth0 authentication. 
            Please log in to access the chat.
          </p>
          <button className="login-button" onClick={() => loginWithRedirect()}>
            Log In
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          <h1 className="app-title">WE-ii Chat</h1>
          <div>
            <span style={{ marginRight: '15px' }}>
              {user?.name || user?.email}
            </span>
            <button 
              className="auth-button" 
              onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}
            >
              Log Out
            </button>
          </div>
        </div>
      </header>
      <ChatInterface />
    </div>
  );
}

export default ChatApp;
