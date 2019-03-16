import sys

from glacier_service import GlacierService

def main():
  args = sys.argv

  if len(args) <= 3:
    print("Too few arguments: Vault name, region and filename are required!")
    return 1

  glacier = GlacierService(args[1], args[2])

  if args[3] == "meta":
    glacier.get_vault_metadata()
    return 0
  
  glacier.upload_archive(args[3], 4*1024*1024*1024)

main()