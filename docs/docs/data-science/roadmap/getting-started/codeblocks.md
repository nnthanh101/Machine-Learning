---
title: TEMP - Codeblocks
sidebar_position: 6
---

```jsx title="Codeblock"
function Greeting(props) {
  return <p>Welcome, {props.userName}!</p>;
}

export default Greeting;
```

```jsx title="Highlight Lines"
function HighlightText(highlight) {
  if (highlight) {
    // highlight-next-line
    return 'This text is highlighted!';
  }
  return 'Nothing highlighted';
}

function HighlightMoreText(highlight) {
  // highlight-start
  if (highlight) {
    return 'This range is highlighted!';
  }
  // highlight-end
  return 'Highlighted';
}
```

```jsx title="Line Numbers" showLineNumbers
import React from 'react';

function UserProfile(props) {
  const { username, email, isAdmin } = props;

  return (
    <div>
      <h1>User Profile</h1>
      <p>Username: {username}</p>
      <p>Email: {email}</p>
      {isAdmin && <p>Admin User</p>}
    </div>
  );
}

export default UserProfile;
```

```jsx title="Line Numbers with Highlight" {4,9-11} showLineNumbers
import React from 'react';

function UserProfile(props) {
  const { username, email, isAdmin } = props;

  return (
    <div>
      <h1>User Profile</h1>
      <p>Username: {username}</p>
      <p>Email: {email}</p>
      {isAdmin && <p>Admin User</p>}
    </div>
  );
}

export default UserProfile;
```
