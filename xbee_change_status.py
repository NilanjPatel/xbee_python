import serial
from xbee import ZigBee,XBee
import struct


serial_port = serial.Serial('COM5', 9600)
xbee1 = ZigBee(serial_port)
xbee2 = XBee(serial_port)

address =(struct.pack(">H",6900))
low = struct.pack(">H",4)
high = struct.pack(">H",5)
print(address,low,high)

while True:
    try:
        data=xbee1.wait_read_frame()
        print(data)
        samples = data['samples']
        dio=samples[0]
        status=(dio['dio-3'])

        try:
            if status==False :
                print(status)
                xbee2.send('remote_at',
                       frame_id='B',
                       dest_addr_long='\x00\x13\xA2\x00\x41\x24\x1E\x74',
                       dest_addr='\x1a\xf4',
                       options='\x02',
                       command='D3',
                       parameter='\x05')
            elif status==True:
                print(status)
                xbee2.send('remote_at',
                 frame_id='B',
                 dest_addr_long='\x00\x13\xA2\x00\x41\x24\x1E\x74',
                 dest_addr='\x1a\xf4',
                 options='\x02',
                 command='D3',
                 parameter='\x04')

        except Exception as e:
            print("Exception for:" , e)
    except Exception as e:
        print("Exception:",e)


serial_port.close()
