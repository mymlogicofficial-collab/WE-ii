import React from 'react';
import { Auth0Provider } from '@auth0/auth0-react';
import ChatApp from './components/ChatApp';
import './App.css';

function App() {
  // These values should be configured via environment variables
  // See README.md for configuration instructions
  const domain = process.env.REACT_APP_AUTH0_DOMAIN || '';
  const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID || '';
  const audience = process.env.REACT_APP_AUTH0_AUDIENCE || '';

  return (
    <Auth0Provider
      domain={domain}
      clientId={clientId}
      authorizationParams={{
        redirect_uri: window.location.origin,
        audience: audience,
        scope: "openid profile email"
      }}
    >
      <ChatApp />
    </Auth0Provider>
  );
}

export default App;
