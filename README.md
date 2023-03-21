# digitalocean-scheduler

### Before runnig

Add `TOKEN` as environment variable before deployment (this is the Digital Ocean token)
### Add droplets to the snapshot process
To add droplets you have to give it this tag `backup-true`

### Deploy the function

`doctl serverless deploy .`

### Get volume ID

`doctl compute volume ls`

```
doctl compute droplet-action snapshot 340456218 --snapshot-name '<snapshot-name>'
doctl compute volume snapshot <volume-id> --snapshot-name '<snapshot-name>'

```