import sys,struct
LT={0:'HDA',1:'DSP',2:'PDM(DMIC)',3:'SSP(I2S)'}; DT={0:'BT',1:'DMIC',2:'I2S',4:'I2S-PCM'}
AT={0x0A:'2 Mics klein',0x0B:'2 Mics gross',0x0C:'4 Mics L-Form',0x0D:'4 Mics linear',0x0E:'Vendor-defined'}
for fn in sys.argv[1:]:
    b=open(fn,'rb').read(); n=b[36]; i=37; print('==',fn.split('/')[-3] if 'captures' in fn else 'Dell 5420', 'Endpoints:',n)
    for e in range(n):
        L=struct.unpack('<I',b[i:i+4])[0]; lt,inst=b[i+4],b[i+5]; vid,did=struct.unpack('<HH',b[i+6:i+10]); dtyp,dirn,vb=b[i+16],b[i+17],b[i+18]
        cs=struct.unpack('<I',b[i+19:i+23])[0]; cfg=b[i+23:i+23+cs]; extra=''
        if lt==2 and cs>=3: extra=f' Array: {AT.get(cfg[2],hex(cfg[2]))}' if cfg[1]==1 else f' cfgtype {cfg[1]}'
        if lt==2 and cs>=3 and cfg[2]==0x0E and len(cfg)>=5: extra+=f' ({cfg[4]} Mics)' if len(cfg)>4 else ''
        print(f'  {LT.get(lt,lt)} dev {DT.get(dtyp,dtyp)} dir {"in" if dirn==1 else "out" if dirn==0 else dirn} vbus {vb} id {vid:04x}:{did:04x}{extra}')
        i+=L
