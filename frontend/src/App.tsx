import { useEffect, useState } from 'react';
import { fetchTodayMessage, subscribeEmail, MessageResponse } from './api';
import { animateMessage } from './animations';
import './styles.css';

// Default fallback values
const defaultData: MessageResponse = {
  message: "The start you deserve, every day.",
  image_url: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80"
};

function App() {
  const [data, setData] = useState<MessageResponse | null>(null);
  const [email, setEmail] = useState<string>('');
  const [status, setStatus] = useState<string>('');

  useEffect(() => {
    fetchTodayMessage()
      .then((res) => setData(res || defaultData))
      .catch(() => setData(defaultData));
  }, []);

  useEffect(() => {
    if (data) animateMessage();
  }, [data]);

  const handleSubscribe = async () => {
    try {
      await subscribeEmail(email);
      setStatus('Subscribed successfully!');
    } catch {
      setStatus('Subscription failed.');
    }
  };

  if (!data) return <div>Loading...</div>;

  // Use fallback if data is null (shouldn't happen, but for safety)
  const displayData = data || defaultData;

  return (
    <div className="container" style={{ backgroundImage: `url(${displayData.image_url})` }}>
      <h1 className="message">{displayData.message}</h1>
      <div className="subscribe">
        <input
          type="email"
          placeholder="Your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button onClick={handleSubscribe}>Subscribe</button>
      </div>
      {status && <p>{status}</p>}
    </div>
  );
}

export default App;