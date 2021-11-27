import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def uploadFile(self,filefrom,fileto):
        debx = dropbox.Dropbox(self.accessToken)
        f = open(filefrom,'rb')
        debx.files_upload(f.read(),fileto)
def main():
    accessToken = 'sl.A9HrBtAOMMO20vO6tPdsQVHYv2r2OQEIcnFJ-INVB30QVMEMkJk_23hA2DwvN0Ix_MnMD76fXHllI6Os2HJKPR8MCSbskn3Y7P6j7ANWrSMXEtvLkDxF21zb-I-wzmbO9ynaukw'
    transferdata = TransferData(accessToken)
    filefrom = input("Enter the file path to transfer")
    fileto = input("Enter full path to upload in the dropbox")
    transferdata.uploadFile(filefrom,fileto)
    print("Transfer Complete")
main()

