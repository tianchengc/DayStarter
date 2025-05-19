export interface MessageResponse {
  message: string;
  image_url: string;
}

export async function fetchTodayMessage(): Promise<MessageResponse> {
  const res = await fetch('/api/message/today');
  if (!res.ok) throw new Error('Failed to load message');
  return res.json();
}

export async function subscribeEmail(email: string): Promise<void> {
  const res = await fetch('/api/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email }),
  });
  if (!res.ok) throw new Error('Subscription failed');
}