import os, sys
try:
    from ppadb.client import Client as AdbClient
except ImportError:
    print("[-] Error: %s -m pip install pure-python-adb" % sys.executable)
    sys.exit() 

from base64 import b64decode,b64encode
client = AdbClient(host="127.0.0.1", port=5037)

if len(sys.argv) < 2:
    print(f"""
    For full setup and certificates export use the argument 'full'
    if you wish only to export burp certificates use the argument 'export'
    Examples:\n
    Usage: python3 {sys.argv[0]} full
    Usage: python3 {sys.argv[0]} export
    
    """)

def export_cert():
     cert = """-----BEGIN CERTIFICATE-----
MIIDqDCCApCgAwIBAgIFAPKNPNUwDQYJKoZIhvcNAQELBQAwgYoxFDASBgNVBAYT
C1BvcnRTd2lnZ2VyMRQwEgYDVQQIEwtQb3J0U3dpZ2dlcjEUMBIGA1UEBxMLUG9y
dFN3aWdnZXIxFDASBgNVBAoTC1BvcnRTd2lnZ2VyMRcwFQYDVQQLEw5Qb3J0U3dp
Z2dlciBDQTEXMBUGA1UEAxMOUG9ydFN3aWdnZXIgQ0EwHhcNMTQwODE3MDcwMTA3
WhcNMzAwODE3MDcwMTA3WjCBijEUMBIGA1UEBhMLUG9ydFN3aWdnZXIxFDASBgNV
BAgTC1BvcnRTd2lnZ2VyMRQwEgYDVQQHEwtQb3J0U3dpZ2dlcjEUMBIGA1UEChML
UG9ydFN3aWdnZXIxFzAVBgNVBAsTDlBvcnRTd2lnZ2VyIENBMRcwFQYDVQQDEw5Q
b3J0U3dpZ2dlciBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMOC
1rNbYz9ZORCO9y7NN4Tp5uXiIrDDEcU2q9puG8EhFsYLKhZ8BGaFVEU1ZMpL3baJ
gTnbwvdQeBBchzNbai0bo8T5iKAsHK1s80tozy4G4kpO4ksGoEYSwTq+vwdDb7NV
PCNzVpeA+6ZdTmzwRgSZygJN8gzT2Ftrt2wYvJpYwSl9rcPseknISraa1ubjuz36
24mnp1rhpHlAI0ybiy9kXH33djmk5u2QyX1jbbzqYuKo1E1ldb0PnksxIJhkfZQC
WE1F4G4WLZuOHDVzdB/vPnesr0+vxxS/opZezz55gG/+GJUgyvbKGgLsiPnEGRA8
6hL0ItbMvkEtrqqPWGcCAwEAAaMTMBEwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG
9w0BAQsFAAOCAQEAfVwMso3MT1itVWh51c7Q7w+12L2wtBZ6XsVZiwQdTH7Vwm7x
RHz0lCUh4CaMS5XYb4Uk9LfnNYfeFLAw0KuYrK7w3cX6WObODOy9TBj3s2VetaAj
f8gWdo13Lc0kuUVRo7KMHLemmkBovDVmjboYAL4SS9KZzESvlt+6WsMVCsrKnjrU
9zmTlUTaFQFE+Gk0gvlv5SusXi9SCVJK6YLj9i/nHQRaXOJ9z4JuOoxa5CX8S2zH
tNn2TRRFm7m7UwcbfG76umevpzNYt9ZCgm3a3AE2VWHXttshfPdUJ5cxhGGOfLuo
y3J/3ClUn8x+IeuuLlYYYqIkf72U6bQjuyCsDw==
-----END CERTIFICATE-----"""

     with open("9a5ba575.0", "w+") as file:
         file.write(cert)

def pushinto_device():
    for device in client.devices():
        device.push(os.getcwd() + "\\9a5ba575.0", "/sdcard/9a5ba575.0")
        device.root()
        device.remount()
        device.shell("mount -o rw,remount /system ; mv /sdcard/9a5ba575.0 /system/etc/security/cacerts/ ; chmod 644 /system/etc/security/cacerts/9a5ba575.0 ; chown root:root /system/etc/security/cacerts/9a5ba575.0")
        # device.shell("mv /sdcard/9a5ba575.0 /system/etc/security/cacerts/")
        # device.shell("chmod 644 /system/etc/security/cacerts/9a5ba575.0")
        # device.shell("chown root:root /system/etc/security/cacerts/9a5ba575.0")
        input("[+] Hit Enter to restart the device and finish the proccess")
        device.reboot()
        print("[+] Rebooting!\n[+] Deleting certificate from file system")
        #os.remove("9a5ba575.0")

def export_burp_certs():
    try:
        priv_key = b'MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDDgtazW2M/WTkQjvcuzTeE6ebl4iKwwxHFNqvabhvBIRbGCyoWfARmhVRFNWTKS922iYE528L3UHgQXIczW2otG6PE+YigLBytbPNLaM8uBuJKTuJLBqBGEsE6vr8HQ2+zVTwjc1aXgPumXU5s8EYEmcoCTfIM09hba7dsGLyaWMEpfa3D7HpJyEq2mtbm47s9+tuJp6da4aR5QCNMm4svZFx993Y5pObtkMl9Y2286mLiqNRNZXW9D55LMSCYZH2UAlhNReBuFi2bjhw1c3Qf7z53rK9Pr8cUv6KWXs8+eYBv/hiVIMr2yhoC7Ij5xBkQPOoS9CLWzL5BLa6qj1hnAgMBAAECggEAVCshrzlqsr0AmiZSN+3VNv1TkCgYcyynm9V7ip/Yhv5txXjM970QT+qaaukfqQ+cNZdg8L2xY7Na3QBYnD2Aqka57HTY4sva1LaQzygh+VixVvg6573EhiZQ1a+EoeXgUr4hE8n1v2eh7u9AchnGqvhiRTe1OtyAymrHHlxP5coLSeC/cNdOdIdXaKCm6/bws4pQFi+S6Co/ZfXf3byyorcmOIqVBAuVXXuH9v338qBL8VXSoVOXjuOFnoiXoG0x+3DSu/OaVKQZ7J8i+4+AcZE8qDpzdcgaohIHvUIOEkUd0dd++NQ8yRnKGEUnPBVJ8FlFtFDhXYcbSE4BWLZUwQKBgQDigRYIFbDoZfdd3HTBBrD+WfWVQQKCvD1TYW1SotL8DwzknCl+mIpXdOcuShnlQICPZ9qWz52CfHF1oft5W5ZJG1dlLMwtW5eG27+fq48KPvsC8TRiZh2FHPwYyf4R7JnUwkGcLRyQpTR3oHj8yH7ujAlg6r2eQPyng0f/06nFsQKBgQDc+Iqx/O32IrKHjkaJUk7SyjAtb5wdMy7Rm72jm5G3JVWEn8KhIop/IRz4zERoO7w1WZSfrKcdPYE++zbLilu/fWo8YRys4cQc7ykiagoyFchsb7QZAoJgEnhgAyEaoPvjb416UQNlg7zW1DQlfL0naqOqbJ82AUHPEP+1fi3NlwKBgQDZeEz56DGZgEUXtlHW/qCzJRY4fll1wlwzESjQnYpq/dxIJnNkm/q/a3uHIxhn1x1YEsN55s54+RhKdAKpizjo6jpn5rIGnpkGnzgFisdkdAG22nWMQDT5mFGnT1EETqGH+BbcZye07RlJ/iYLtkjAqm1awybZqdWq084uH0AykQKBgQCfzg9gEW925jj+1+IjRadDwn19Ho5kf7OIW32WaNfE//cM5w02w2gt8KCnPfLq/uhqHNLjd1WUS/rAtaU3JmSb4/OEnybB0LSnyD6TaOTeu+oqoc45mBr5p+HubdTvESWZof9LSnOOYuua4fSkd8XET9b1VYD+6YHSYpTLiOlPGQKBgQCp8Uojdk98uJfWywFDC9P2aEUy8H3Pvy2F25OmxvlxsEN7j68EWy8O3vwuUCJk5+GF6pWw9hON+9zywu1J7Hcybvwky80hQ+gTBvYqiXb+wXWvV7s3SzbzhG+Zn/Oi3WCe7pw+OY9Qjnin/Vgr0/x1yADPSUY5sl2GHJFX6UkiCA=='
        cert = b'MIIDqDCCApCgAwIBAgIFAPKNPNUwDQYJKoZIhvcNAQELBQAwgYoxFDASBgNVBAYTC1BvcnRTd2lnZ2VyMRQwEgYDVQQIEwtQb3J0U3dpZ2dlcjEUMBIGA1UEBxMLUG9ydFN3aWdnZXIxFDASBgNVBAoTC1BvcnRTd2lnZ2VyMRcwFQYDVQQLEw5Qb3J0U3dpZ2dlciBDQTEXMBUGA1UEAxMOUG9ydFN3aWdnZXIgQ0EwHhcNMTQwODE3MDcwMTA3WhcNMzAwODE3MDcwMTA3WjCBijEUMBIGA1UEBhMLUG9ydFN3aWdnZXIxFDASBgNVBAgTC1BvcnRTd2lnZ2VyMRQwEgYDVQQHEwtQb3J0U3dpZ2dlcjEUMBIGA1UEChMLUG9ydFN3aWdnZXIxFzAVBgNVBAsTDlBvcnRTd2lnZ2VyIENBMRcwFQYDVQQDEw5Qb3J0U3dpZ2dlciBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMOC1rNbYz9ZORCO9y7NN4Tp5uXiIrDDEcU2q9puG8EhFsYLKhZ8BGaFVEU1ZMpL3baJgTnbwvdQeBBchzNbai0bo8T5iKAsHK1s80tozy4G4kpO4ksGoEYSwTq+vwdDb7NVPCNzVpeA+6ZdTmzwRgSZygJN8gzT2Ftrt2wYvJpYwSl9rcPseknISraa1ubjuz3624mnp1rhpHlAI0ybiy9kXH33djmk5u2QyX1jbbzqYuKo1E1ldb0PnksxIJhkfZQCWE1F4G4WLZuOHDVzdB/vPnesr0+vxxS/opZezz55gG/+GJUgyvbKGgLsiPnEGRA86hL0ItbMvkEtrqqPWGcCAwEAAaMTMBEwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAfVwMso3MT1itVWh51c7Q7w+12L2wtBZ6XsVZiwQdTH7Vwm7xRHz0lCUh4CaMS5XYb4Uk9LfnNYfeFLAw0KuYrK7w3cX6WObODOy9TBj3s2VetaAjf8gWdo13Lc0kuUVRo7KMHLemmkBovDVmjboYAL4SS9KZzESvlt+6WsMVCsrKnjrU9zmTlUTaFQFE+Gk0gvlv5SusXi9SCVJK6YLj9i/nHQRaXOJ9z4JuOoxa5CX8S2zHtNn2TRRFm7m7UwcbfG76umevpzNYt9ZCgm3a3AE2VWHXttshfPdUJ5cxhGGOfLuoy3J/3ClUn8x+IeuuLlYYYqIkf72U6bQjuyCsDw=='
        with open("private-key1.der", "wb") as binary:
            binary.write(b64decode(priv_key))
        with open("cacert1.der", "wb") as binary:
            binary.write(b64decode(cert))
    except Exception as err:
        print(err)
    else:
        print("[+] Done!\nnow use the generated certificates, to import the certificates into burp use:\n\tProxy --> Options --> Import / export CA certificate --> import certificate and private key in DER format")
    
""" 
def encode_certs():
    with open(sys.argv[1], "rb") as file1:
        print(b64encode(file1.read()))
        with open("omri.cert", "wb") as binary:
            binary.write(file1.read())
"""        # I used this function to base64 encode the priv and cacert in order to add them into the script

try:
    if len(sys.argv) == 2:
        if sys.argv[1] == "export":
            print("[+] Only exporting burp certificates.")
            export_burp_certs()
            sys.exit()
        if sys.argv[1] == "full":
            export_cert()
            pushinto_device()
            export_burp_certs()
            #encode_certs()

except RuntimeError:
    print("Are you sure a device is connected bro?")
except ConnectionRefusedError:
    print("Are you sure a device is connected bro?")
except Exception as err:
    print(err)
