import ctypes, wmi

# WMI-Verbindung initialisieren
c = wmi.WMI()

# Abfrage der Win32_PerfRawData_PerfOS_Memory Klasse
memory_info = c.Win32_PerfRawData_PerfOS_Memory()[0]

# Abfrage der gesamten physischen Speichergröße
total_physical_memory_info = c.Win32_ComputerSystem()[0]
total_physical_memory_bytes = float(total_physical_memory_info.TotalPhysicalMemory)

# Umrechnungsfaktor von Bytes zu Gigabytes
bytes_to_gb = 1024 ** 3

# Berechnung des wirklich freien Speichers
available_bytes = float(memory_info.AvailableBytes)
standby_cache_reserve_bytes = float(memory_info.StandbyCacheReserveBytes)
standby_cache_normal_priority_bytes = float(memory_info.StandbyCacheNormalPriorityBytes)
standby_cache_core_bytes = float(memory_info.StandbyCacheCoreBytes)

# Gesamter physischer Speicher in GB
total_physical_memory_gb = round(total_physical_memory_bytes / bytes_to_gb, 2)

# Berechnung des gesamten Standby-Cache-Speichers
total_standby_cache_bytes = standby_cache_reserve_bytes + standby_cache_normal_priority_bytes + standby_cache_core_bytes

# Wirklich freier Speicher
real_free_memory_gb = round((available_bytes - total_standby_cache_bytes) / bytes_to_gb, 2)

# Gesamter Cache-Speicher
total_cache_memory_gb = round(total_standby_cache_bytes / bytes_to_gb, 2)

def allocate_and_free_memory(size_in_gb):
    try:
        size_in_bytes = round(size_in_gb * (1024 ** 3))  # Korrekte Umrechnung von GB in Bytes
        buffer = ctypes.create_string_buffer(size_in_bytes)
        print(f"{size_in_gb} GB Speicher wurden zugewiesen und werden automatisch freigegeben.")
    except MemoryError:
        print(f"Fehler: Konnte nicht {size_in_gb} GB Speicher allokieren.")

if __name__ == '__main__':
    print(f"Wirklich freier Speicher: {real_free_memory_gb} GB")
    print(f"Gesamter Cache-Speicher: {total_cache_memory_gb} GB")
    print(f"Halber Cache-Speicher: {total_cache_memory_gb / 4} GB")

    if real_free_memory_gb < 1 or (real_free_memory_gb / total_physical_memory_gb) * 100 < 5:
        allocate_and_free_memory(total_cache_memory_gb / 2)  # 1 GB Speicher allokieren und freigeben