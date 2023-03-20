# digitalocean-scheduler

### Before runnig

Add `TOKEN` as environment variable before deployment (this is the Digital Ocean token)

### Deploy the function

`doctl serverless deploy .`
```
doctl compute droplet-action snapshot 340456218 --snapshot-name '<snapshot-name>'
doctl compute volume snapshot <volume-id> --snapshot-name '<snapshot-name>'

```