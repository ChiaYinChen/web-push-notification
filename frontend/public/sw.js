this.addEventListener('activate', function (event){
  console.log('service worker activated');
});

this.addEventListener('push', async function (event){
  console.log('notifications will be displayed here');
  console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);
  const message = await event.data.json();
  let {title, description} = message;
  console.log({message});
  await event.waitUntil (
    this.registration.showNotification(title, {
      body: description,
      icon: '/logo192.png',
      actions: [
        {
          action: 'Detail',
          title: 'say hi',
        },
      ],
    })
  );
});