import ctypes, psutil
import win32com.client

# Umrechnungsfaktor von Bytes zu Gigabytes
bytes_to_gb = 1024 ** 3

# Verfügbarer Speicher in GB
free_memory_gb = round(psutil.virtual_memory().available / bytes_to_gb, 2)

# Standby-Speicher für Windows ermitteln
def get_standby_memory_gb():
    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
    colItems = objSWbemServices.ExecQuery("Select * from Win32_PerfRawData_PerfOS_Memory")
    for objItem in colItems:
        standby_bytes = objItem.StandbyCacheReserveBytes + objItem.StandbyCacheNormalPriorityBytes + objItem.StandbyCacheCoreBytes
        return round(standby_bytes / bytes_to_gb, 2)
    return 0

standby_memory_gb = get_standby_memory_gb()

# Unbenutzter Speicher in GB
unused_memory_gb = free_memory_gb - standby_memory_gb

print(f"Freier Speicher: {free_memory_gb} GB")
print(f"Standby-Speicher: {standby_memory_gb} GB")
print(f"Unbenutzter Speicher: {unused_memory_gb} GB")

def allocate_and_free_memory(size_in_mb):
    size = size_in_mb * 1024 * 1024  # Umrechnung von MB in Bytes

    buffer = ctypes.create_string_buffer(size)

    print(f"{size_in_mb} MB Speicher wurden zugewiesen und werden automatisch freigegeben.")

if __name__ == '__main__':
    allocate_and_free_memory(1024)  # 1024 MB Speicher allokieren und freigeben