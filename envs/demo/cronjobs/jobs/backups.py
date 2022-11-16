import tarfile
import os
from datetime import datetime

date_time = datetime.now()
str_date = date_time.strftime("%Y%m%d%H%M%S")

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

# iterate over directories in /opt/volumes and create a tar file in /opt/backups for each of them
for volume in os.listdir('/opt/volumes'):
    make_tarfile("/opt/backups/" + volume + "-" + str_date + ".tar.gz" , "/opt/volumes/" + volume)