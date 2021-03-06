__author__ = 'igorkhomenko'

from boto.glacier.layer1 import Layer1
from boto.glacier.concurrent import ConcurrentUploader


class GlacierService:

    def __init__(self, target_vault_name, region_name):
        self.target_vault_name = target_vault_name
        self.region_name = region_name

    def upload_archive(self, file_name, partSize=32*1024*1024):
        glacier_layer1 = Layer1(region_name=self.region_name)

        uploader = ConcurrentUploader(
            glacier_layer1, self.target_vault_name, partSize)

        print("operation starting...")

        archive_id = uploader.upload(file_name, file_name)

        print("Success! archive id: '%s'" % archive_id)

    def delete_archive(self, archive_id):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        print(glacier_layer1.delete_archive(
            self.target_vault_name, archive_id))

    def initiate_archive_retrieval_job(self, archive_id):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        job_id = glacier_layer1.initiate_job(self.target_vault_name, {"Description": "download-archive-job",
                                                                      "Type": "archive-retrieval",
                                                                      "ArchiveId": archive_id})

        print("Success! job id: %s" % (job_id,))

        return job_id

    def get_vault_metadata(self):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        vault_metadata = glacier_layer1.describe_vault(self.target_vault_name)

        print("Success! vault metadata: %s" % vault_metadata)

    def list_jobs(self, job_id=None):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        if(job_id != None):
            print(glacier_layer1.describe_job(self.target_vault_name, job_id))
        else:
            print(glacier_layer1.list_jobs(
                self.target_vault_name, completed=False))

    def get_job_output(self, job_id=None):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        output = glacier_layer1.get_job_output(self.target_vault_name, job_id)
        print(output)

        return output

    def initiate_vault_inventory_job(self):
        glacier_layer1 = Layer1(region_name=self.region_name)

        print("operation starting...")

        job_id = glacier_layer1.initiate_job(self.target_vault_name, {"Description": "inventory-job",
                                                                      "Type": "inventory-retrieval",
                                                                      "Format": "JSON"})

        print("Success! inventory job id: %s" % (job_id,))

        return job_id
