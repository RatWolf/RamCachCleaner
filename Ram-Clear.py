import ctypes, wmi

c = wmi.WMI() # WMI-Verbindung initialisieren
memory_info = c.Win32_PerfRawData_PerfOS_Memory()[0] # Abfrage der Win32_PerfRawData_PerfOS_Memory Klasse
total_physical_memory_info = c.Win32_ComputerSystem()[0] # Abfrage der Win32_ComputerSystem Klasse
total_physical_memory_bytes = float(total_physical_memory_info.TotalPhysicalMemory) # Gesamter physischer Speicher in Bytes
bytes_to_gb = 1024 ** 3 # Umrechnungsfaktor von Bytes zu Gigabytes

available_bytes = float(memory_info.AvailableBytes) # Verfügbare Bytes
standby_cache_reserve_bytes = float(memory_info.StandbyCacheReserveBytes) # Standby-Cache-Reserve-Bytes
standby_cache_normal_priority_bytes = float(memory_info.StandbyCacheNormalPriorityBytes) # Standby-Cache-Normal-Prioritäts-Bytes
standby_cache_core_bytes = float(memory_info.StandbyCacheCoreBytes) # Standby-Cache-Core-Bytes

total_physical_memory_gb = round(total_physical_memory_bytes / bytes_to_gb, 2) # Gesamter physischer Speicher in GB
total_standby_cache_bytes = standby_cache_reserve_bytes + standby_cache_normal_priority_bytes + standby_cache_core_bytes # Berechnung des gesamten Standby-Cache-Speichers
real_free_memory_gb = round((available_bytes - total_standby_cache_bytes) / bytes_to_gb, 2) # Wirklich freier Speicher
total_cache_memory_gb = round(total_standby_cache_bytes / bytes_to_gb, 2) # Gesamter Cache-Speicher

def allocate_and_free_memory(size_in_gb): # Funktion zum Allokieren und Freigeben von Speicher
    try:
        size_in_bytes = round(size_in_gb * (1024 ** 3))  # Korrekte Umrechnung von GB in Bytes
        buffer = ctypes.create_string_buffer(size_in_bytes) # Speicher allokieren
        print(f"{size_in_gb} GB Speicher wurden zugewiesen und werden automatisch freigegeben.")
    except MemoryError:
        print(f"Fehler: Konnte nicht {size_in_gb} GB Speicher allokieren.")

if __name__ == '__main__':
    toFree = min(1, total_physical_memory_gb * 0.05) # Mindestens 1 GB oder 5% des gesamten physischen Speichers freigeben

    if real_free_memory_gb < toFree and total_cache_memory_gb > toFree: # Wenn der wirklich freie Speicher kleiner als der freizugebende Speicher ist und der Cache-Speicher größer als der freizugebende Speicher ist
        allocate_and_free_memory(total_cache_memory_gb / 2)  # 1 GB Speicher allokieren und freigeben