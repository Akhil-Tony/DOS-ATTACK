import pandas as pd
import re

def process_log_data(log_data):
    # Extracting lines containing the FTM Report data using regular expressions

    ap_name_pattern = r'Scanning for (\S+)'
    ap_name_match = re.search(ap_name_pattern, log_data)
    ap_name = ap_name_match.group(1) if ap_name_match else None

    ap_name = ap_name.replace('\x1b[0m', '').strip()

    data_lines = re.findall(r'I \(\d+\) ftm_station: \|.*', log_data)

    # Remove lines containing the specified patterns
    cleaned_data = [re.sub(r'I \(\d{4}\) ftm_station: ', '', line) for line in data_lines][1:]

    # Replace '\x1b[0m' with the value before 'm'
    cleaned_data = [re.sub(r'\x1b\[(\d+)m', r'\1', line) for line in cleaned_data]

    cleaned_data = [line.strip('|').split('|') for line in cleaned_data]
    append_data_row = []

    for line in cleaned_data:
        append_data_row.append([item.strip() for item in line if item.strip()])

    # Extracting additional values from the log data
    estimated_rtt_pattern = r'Estimated RTT - (\d+) nSec'
    estimated_distance_pattern = r'Estimated Distance - ([\d.]+) meters'
    avg_rtt_pattern = r'Avg raw RTT: ([\d.]+) nSec'
    avg_rssi_pattern = r'Avg RSSI: (-\d+)'

    estimated_rtt = re.search(estimated_rtt_pattern, log_data).group(1)
    print()
    estimated_distance = re.search(estimated_distance_pattern, log_data).group(1)
    avg_rtt = re.search(avg_rtt_pattern, log_data).group(1)
    avg_rssi = re.search(avg_rssi_pattern, log_data).group(1)

    # Creating a DataFrame
    column_names = ["Diag", "RTT", "T1", "T2", "T3", "T4", "RSSI", "Actual Meter"]
    df = pd.DataFrame(append_data_row, columns=column_names)
    
    # Adding the extracted values
    df["Estimated_RTT"] = estimated_rtt
    df["Estimated_Distance"] = estimated_distance
    df["Avg_RTT"] = avg_rtt
    df["Avg_RSSI"] = avg_rssi
    df["ap_name"] = ap_name

    return df
    



# The raw log data
log_data = """
============ PuTTY log 2023.08.10 18:32:09 ============
ESP-ROM:esp32c3-api1-20210207
Build:Feb  7 2021
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fcd5820,len:0x1708
load:0x403cc710,len:0x968
load:0x403ce710,len:0x2f68
entry 0x403cc710
[0;32mI (30) boot: ESP-IDF v5.1-dirty 2nd stage bootloader[0m
[0;32mI (30) boot: compile time Jul 31 2023 18:27:37[0m
[0;32mI (30) boot: chip revision: v0.4[0m
[0;32mI (34) boot.esp32c3: SPI Speed      : 80MHz[0m
[0;32mI (38) boot.esp32c3: SPI Mode       : DIO[0m
[0;32mI (43) boot.esp32c3: SPI Flash Size : 2MB[0m
[0;32mI (48) boot: Enabling RNG early entropy source...[0m
[0;32mI (53) boot: Partition Table:[0m
[0;32mI (57) boot: ## Label            Usage          Type ST Offset   Length[0m
[0;32mI (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000[0m
[0;32mI (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000[0m
[0;32mI (79) boot:  2 factory          factory app      00 00 00010000 00100000[0m
[0;32mI (86) boot: End of partition table[0m
[0;32mI (91) esp_image: segment 0: paddr=00010020 vaddr=3c0a0020 size=20ba0h (134048) map[0m
[0;32mI (120) esp_image: segment 1: paddr=00030bc8 vaddr=3fc91600 size=02864h ( 10340) load[0m
[0;32mI (123) esp_image: segment 2: paddr=00033434 vaddr=40380000 size=0cbe4h ( 52196) load[0m
[0;32mI (136) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=9423ch (606780) map[0m
[0;32mI (233) esp_image: segment 4: paddr=000d4264 vaddr=4038cbe4 size=04948h ( 18760) load[0m
[0;32mI (242) boot: Loaded app from partition at offset 0x10000[0m
[0;32mI (243) boot: Disabling RNG early entropy source...[0m
[0;32mI (254) cpu_start: Unicore app[0m
[0;32mI (254) cpu_start: Pro cpu up.[0m
[0;32mI (263) cpu_start: Pro cpu start user code[0m
[0;32mI (263) cpu_start: cpu freq: 160000000 Hz[0m
[0;32mI (263) cpu_start: Application information:[0m
[0;32mI (266) cpu_start: Project name:     ftm[0m
[0;32mI (270) cpu_start: App version:      1[0m
[0;32mI (275) cpu_start: Compile time:     Jul 31 2023 18:22:17[0m
[0;32mI (281) cpu_start: ELF file SHA256:  e730675a99122572...[0m
[0;32mI (287) cpu_start: ESP-IDF:          v5.1-dirty[0m
[0;32mI (292) cpu_start: Min chip rev:     v0.3[0m
[0;32mI (297) cpu_start: Max chip rev:     v0.99 [0m
[0;32mI (302) cpu_start: Chip rev:         v0.4[0m
[0;32mI (306) heap_init: Initializing. RAM available for dynamic allocation:[0m
[0;32mI (314) heap_init: At 3FC98A70 len 00043CA0 (271 KiB): DRAM[0m
[0;32mI (320) heap_init: At 3FCDC710 len 00002950 (10 KiB): STACK/DRAM[0m
[0;32mI (327) heap_init: At 50000020 len 00001FE0 (7 KiB): RTCRAM[0m
[0;32mI (334) spi_flash: detected chip: generic[0m
[0;32mI (337) spi_flash: flash io: dio[0m
[0;33mW (341) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.[0m
[0;32mI (355) sleep: Configure to isolate all GPIO pins in sleep state[0m
[0;32mI (361) sleep: Enable automatic switching of GPIO sleep configuration[0m
[0;32mI (368) app_start: Starting scheduler on CPU0[0m
[0;32mI (373) main_task: Started on CPU0[0m
[0;32mI (373) main_task: Calling app_main()[0m
[0;32mI (383) pp: pp rom version: 9387209[0m
[0;32mI (383) net80211: net80211 rom version: 9387209[0m
[0;32mI (393) wifi_init: rx ba win: 6[0m
[0;32mI (393) wifi_init: tcpip mbox: 32[0m
[0;32mI (393) wifi_init: udp mbox: 6[0m
[0;32mI (393) wifi_init: tcp mbox: 6[0m
[0;32mI (403) wifi_init: tcp tx win: 5744[0m
[0;32mI (403) wifi_init: tcp rx win: 5744[0m
[0;32mI (413) wifi_init: tcp mss: 1440[0m
[0;32mI (413) wifi_init: WiFi IRAM OP enabled[0m
[0;32mI (413) wifi_init: WiFi RX IRAM OP enabled[0m
[0;32mI (423) phy_init: phy_version 970,1856f88,May 10 2023,17:44:12[0m
[5n[0;32mI (523) ftm_station: Scanning for ESP32C3_DFR1[0m
[0;32mI (3023) ftm_station: sta scan done[0m
[0;32mI (3023) ftm_station: Requesting FTM session with Frm Count - 32, Burst Period - 200mSec (0: No Preference)[0m
W (3033) wifi:Starting FTM session with dc:54:75:60:bf:69 in 0.077 Sec
W (3033) wifi:Mode: non-ASAP, Bursts: 8, FTM's per burst: 4, Burst Period: 200mSec, Burst Duration: 32000uSec
W (4553) wifi:FTM session ends with 29 valid readings out of 31, Avg raw RTT: 611.461 nSec, Avg RSSI: -40
[0;32mI (4553) ftm_station: FTM Report:[0m
[0;32mI (4563) ftm_station: | Diag |   RTT   |       T1       |       T2       |       T3       |       T4       |  RSSI  |[0m
[0;32mI (4573) ftm_station: |     6| 576938  |71468718377125  | 3121737385937  | 3121854460937  |71468836029063  |   -41  |[0m
[0;32mI (4573) ftm_station: |     8| 618938  |71476855377125  | 3129874393750  | 3129979460937  |71476961063250  |   -41  |[0m
[0;32mI (4593) ftm_station: |     9| 617376  |71480865377125  | 3133884396875  | 3133989460937  |71480971058563  |   -41  |[0m
[0;32mI (4603) ftm_station: |    10| 618938  |71669716377125  | 3322735568750  | 3322852460937  |71669833888250  |   -41  |[0m
[0;32mI (4613) ftm_station: |    11| 606438  |71673756377125  | 3326775559375  | 3326880460937  |71673861885125  |   -41  |[0m
[0;32mI (4623) ftm_station: |    12| 575376  |71677838377125  | 3330857575000  | 3330962460937  |71677943838438  |   -41  |[0m
[0;32mI (4633) ftm_station: |    14| 604875  |71870788377125  | 3523807735937  | 3523924460937  |71870905707000  |   -41  |[0m
[0;32mI (4643) ftm_station: |    15| 617375  |71874855377125  | 3527874751562  | 3527979460937  |71874960703875  |   -40  |[0m
[0;32mI (4653) ftm_station: |    16| 618938  |71878910377125  | 3531929756250  | 3532034460937  |71879015700750  |   -41  |[0m
[0;32mI (4673) ftm_station: |    17| 618938  |71882956377125  | 3535975759375  | 3536080460937  |71883061697625  |   -40  |[0m
[0;32mI (4683) ftm_station: |    18| 618938  |72073756377125  | 3726775928125  | 3726892460937  |72073873528875  |   -41  |[0m
[0;32mI (4693) ftm_station: |    19| 617376  |72077795389625  | 3730814943750  | 3730919460937  |72077900524188  |   -41  |[0m
[0;32mI (4703) ftm_station: |    20| 620500  |72081858377125  | 3734877935937  | 3734982460937  |72081963522625  |   -40  |[0m
[0;32mI (4713) ftm_station: |    21| 618938  |72085913377125  | 3738932939062  | 3739037460937  |72086018517938  |   -41  |[0m
[0;32mI (4723) ftm_station: |    22| 604875  |72272919389625  | 3925939101562  | 3926056460937  |72273037353875  |   -41  |[0m
[0;32mI (4743) ftm_station: |    23| 604876  |72278990377125  | 3932010093750  | 3932114460937  |72279095349188  |   -41  |[0m
[0;32mI (4753) ftm_station: |    24| 618938  |72281037389625  | 3934057121875  | 3934162460937  |72281143347625  |   -41  |[0m
[0;32mI (4763) ftm_station: |    25| 606438  |72285074389625  | 3938094112500  | 3938199460937  |72285180344500  |   -40  |[0m
[0;32mI (4773) ftm_station: |    26| 606438  |72473968389625  | 4126988276562  | 4127105460937  |72474086180438  |   -41  |[0m
[0;32mI (4783) ftm_station: |    27| 617376  |72478053377125  | 4131073278125  | 4131178460937  |72478159177313  |   -41  |[0m
[0;32mI (4793) ftm_station: |    28| 617375  |72483347377125  | 4136367282812  | 4136472460937  |72483453172625  |   -41  |[0m
[0;32mI (4813) ftm_station: |    29| 618938  |72486133389625  | 4139153298437  | 4139258460937  |72486239171063  |   -41  |[0m
[0;32mI (4823) ftm_station: |    30| 617375  |72676406377125  | 4329426448437  | 4329543460937  |72676524007000  |   -40  |[0m
[0;32mI (4833) ftm_station: |    31| 617375  |72680687377125  | 4333707451562  | 4333812460937  |72680793003875  |   -40  |[0m
[0;32mI (4843) ftm_station: |    32| 617375  |72684815377125  | 4337835454687  | 4337940460937  |72684921000750  |   -40  |[0m
[0;32mI (4853) ftm_station: |    33| 617375  |72688669389625  | 4341689470312  | 4341794460937  |72688774997625  |   -41  |[0m
[0;32mI (4863) ftm_station: |    34| 604876  |72876464389625  | 4529484615625  | 4529601460937  |72876581839813  |   -40  |[0m
[0;32mI (4883) ftm_station: |    35| 606438  |72880551377125  | 4533571607812  | 4533676460937  |72880656836688  |   -40  |[0m
[0;32mI (4893) ftm_station: |    36| 606438  |72884606377125  | 4537626610937  | 4537731460937  |72884711833563  |   -40  |[0m
[0;32mI (4903) ftm_station: Estimated RTT - 500 nSec, Estimated Distance - 75.00 meters[0m
[0;32mI (4903) ftm_station: Requesting FTM session with Frm Count - 32, Burst Period - 200mSec (0: No Preference)[0m
W (4913) wifi:Starting FTM session with dc:54:75:60:bf:69 in 0.035 Sec
W (4923) wifi:Mode: non-ASAP, Bursts: 8, FTM's per burst: 4, Burst Period: 200mSec, Burst Duration: 32000uSec
W (6393) wifi:FTM session ends with 30 valid readings out of 31, Avg raw RTT: 451.548 nSec, Avg RSSI: -40
"""

# Call the function and display the DataFrame
df = process_log_data(log_data)
