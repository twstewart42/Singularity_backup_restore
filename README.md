# Singularity_backup_restore

<h2>Singularity_backup.py</h2>
I once crashed <a href="https://github.com/HubSpot/Singularity">Singularity API</a> so hard that it lost all of it's scheduled requests and it was not correctly backing up to it's pre-configured MySQL database. So I created an extrenal backup, that can run independantly of Singularity.


<h2>Singularity_Restore.py</h2>
Of course there is no good use of a backup if you can't restore from it so I created restore-singularity.py. The key to this one was understanding that what came from MySQL was a string and not a <a href="https://github.com/twstewart42/notes-wiki/tree/master/Apache_Mesos_API">JSON</a> object the string would have to be loaded into a python dictionary in order to be segregated into it's separate request and deploy.


This method seems to error for runOnce type tasks, but this is mainly for scheduled tasks that must happen on a regular basis.
<h3>restore</h3>
<pre>
curl -i -X POST -H 'Content-Type: application/json' -d '{"owners": ["me@example.com"], "quartzSchedule": "0 54 * * * ?", "id": "TASK1", "schedule": "54 * * * *"}' app001:8082/singularity/api/requests
curl -i -X POST -H 'Content-Type: application/json' -d '{"resources": {"memoryMb": 512.0, "numPorts": 0, "cpus": 1.0}, "deploy": {"command": "/usr/local/bin/run_command.sh", "requestId": "TASK!", "id": "new_TASK1"}}' app001:8082/singularity/api/deploys
curl -i -X POST -H 'Content-Type: application/json' -d '{"owners": ["me@example.com"], "quartzSchedule": "0 12 5 * * ?", "id": "download_Images", "schedule": "12 5 * * *"}' app001:8082/singularity/api/requests
curl -i -X POST -H 'Content-Type: application/json' -d '{"resources": {"memoryMb": 128.0, "numPorts": 0, "cpus": 0.1}, "deploy": {"command": "doThis_command.php", "requestId": "download_Images", "id": "depdownload_images"}}' app001:8082/singularity/api/deploys
</pre>

