from ophyd import EpicsMotor, PVPositioner, PVPositionerPC, EpicsSignal, EpicsSignalRO, Device
from ophyd import Component as Cpt, FormattedComponent as FmtCpt
from ophyd import (EpicsMCA, EpicsDXP)


# Mirrors

class MirrorAxis(PVPositioner):
    readback = Cpt(EpicsSignalRO, 'Mtr_MON')
    setpoint = Cpt(EpicsSignal, 'Mtr_POS_SP')
    actuate = FmtCpt(EpicsSignal, '{self.parent.prefix}}}MOVE_CMD.PROC')
    actual_value = 1
    stop_signal = FmtCpt(EpicsSignal, '{self.parent.prefix}}}STOP_CMD.PROC')
    stop_value = 1
    done = FmtCpt(EpicsSignalRO, '{self.parent.prefix}}}BUSY_STS')
    done_value = 0


class Mirror(Device):
    z = Cpt(MirrorAxis, '-Ax:Z}')
    y = Cpt(MirrorAxis, '-Ax:Y}')
    x = Cpt(MirrorAxis, '-Ax:X}')
    pit = Cpt(MirrorAxis, '-Ax:Pit}')
    yaw = Cpt(MirrorAxis, '-Ax:Yaw}')
    rol = Cpt(MirrorAxis, '-Ax:Rol}')


class MotorMirror(Device):
    "a mirror with EpicsMotors, used for M3A"
    x = Cpt(EpicsMotor, '-Ax:XAvg}Mtr')
    pit = Cpt(EpicsMotor, '-Ax:P}Mtr')
    bdr = Cpt(EpicsMotor, '-Ax:Bdr}Mtr')



# VLS-PGM

class PGMEnergy(PVPositionerPC):
    readback = Cpt(EpicsSignalRO, '}Enrgy-I')
    setpoint = Cpt(EpicsSignal, '}Enrgy-SP', limits=(200,2200))  # IS THIS LIMITS USAGE CORRECT?
    stop_signal = Cpt(EpicsSignal, '}Cmd:Stop-Cmd')
    stop_value = 1


class PGM(Device):
    energy = Cpt(PGMEnergy, '')
    pit = Cpt(EpicsMotor, '-Ax:MirP}Mtr')
    x = Cpt(EpicsMotor, '-Ax:MirX}Mtr')
    grt_pit = Cpt(EpicsMotor, '-Ax:GrtP}Mtr')
    grt_x = Cpt(EpicsMotor, '-Ax:GrtX}Mtr')



# Slits

class SlitsGapCenter(Device):
    xg = Cpt(EpicsMotor, '-Ax:XGap}Mtr')
    xc = Cpt(EpicsMotor, '-Ax:XCtr}Mtr')
    yg = Cpt(EpicsMotor, '-Ax:YGap}Mtr')
    yc = Cpt(EpicsMotor, '-Ax:YCtr}Mtr')


class SlitsXY(Device):
    x = Cpt(EpicsMotor, '-Ax:X}Mtr', name='x')
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr', name='y')



# Setpoint for PID loop

class PID(PVPositioner):

    ## Calculation side
    #XF:23ID1-OP{FBck}PID.VAL
    #readback = Cpt(EpicsSignalRO, '{FBck}PID-RB')
    #readback = Cpt(EpicsSignalRO, '1-BI{Diag:6-Cam:1}Stats1:CentroidX_RBV')
    readback = Cpt(EpicsSignal, '1-OP{FBck}PID.VAL')
    #setpoint = Cpt(EpicsSignal, '{FBck}PID-SP')
    setpoint = Cpt(EpicsSignal, '1-OP{FBck}PID.VAL')

    ## Movement side
    #XF:23IDA-OP:1{Mir:1}MOVE_CMD.PROC
    #actuate = Cpt(EpicsSignal, '{Mir:1B}MOVE_CMD.PROC')
    actuate = Cpt(EpicsSignal, 'A-OP:1{Mir:1}MOVE_CMD.PROC')
    actual_value = 1
    #stop_signal= Cpt(EpicsSignal, ':2{Mir:1B}STOP_CMD.PROC')
    stop_signal= Cpt(EpicsSignal, 'A-OP:1{Mir:1}STOP_CMD.PROC')
    stop_value = 1
    #done = Cpt(EpicsSignalRO, ':2{Mir:1B}BUSY_STS')
    done = Cpt(EpicsSignalRO, 'A-OP:1{Mir:1}SYSTEM_STS')
    done_value = 0


# Sample position

class SamplePosVirtualMotor(PVPositionerPC):
    readback = Cpt(EpicsSignalRO, 'Pos-RB')
    setpoint = Cpt(EpicsSignal, 'Pos-SP')
    #stop_signal = Cpt(EpicsSignal, 'Cmd:Stop-Cmd')  #PV does not exist and cannot currently compile on ioc2
    stop_value = 1

class Cryoangle(PVPositionerPC):
    readback  = Cpt(EpicsSignalRO, 'XF:23ID1-ES{Dif-Cryo}Pos:Angle-RB')
    setpoint = Cpt(EpicsSignal, 'XF:23ID1-ES{Dif-Cryo}Pos:Angle-SP')
    # TODO original implementation had no stop_signal!!
    stop_value = 1



# Nano-positioners

class Nanopositioner(Device):
    #tx = Cpt(EpicsMotor, '-Ax:TopX}Mtr', settle_time=0.5)
    #ty = Cpt(EpicsMotor, '-Ax:TopY}Mtr', settle_time=0.5)
    #tz = Cpt(EpicsMotor, '-Ax:TopZ}Mtr', settle_time=0.5)
    #bx = Cpt(EpicsMotor, '-Ax:BtmX}Mtr', settle_time=0.5)
    #by = Cpt(EpicsMotor, '-Ax:BtmY}Mtr', settle_time=0.5)
    #bz = Cpt(EpicsMotor, '-Ax:BtmZ}Mtr', settle_time=0.5)
    tx = Cpt(EpicsMotor, '-Ax:TopX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TopY}Mtr')
    tz = Cpt(EpicsMotor, '-Ax:TopZ}Mtr')
    bx = Cpt(EpicsMotor, '-Ax:BtmX}Mtr')
    by = Cpt(EpicsMotor, '-Ax:BtmY}Mtr')
    bz = Cpt(EpicsMotor, '-Ax:BtmZ}Mtr')



## Sample space devices

# Lakeshore 336 Temperature controller

class Lakeshore336(PVPositioner):
    readback = Cpt(EpicsSignalRO, 'T-RB')
    setpoint = Cpt(EpicsSignal, 'T-SP')
    done = Cpt(EpicsSignalRO, 'Sts:Ramp-Sts')
    done_value = 0


# Current-Voltage meter, driven in current mode

class VIMeterVirtualMotorCurr(PVPositionerPC):
    readback = Cpt(EpicsSignalRO, 'Val:RB-I')
    #setpoint = Cpt(EpicsSignal, 'Val:SP-I')
    setpoint = EpicsSignal('XF:23ID1-ES{K2611:1}Val:RB-I','XF:23ID1-ES{K2611:1}Val:SP-I')
    stop_value = 1

class VIMeterVirtualMotorVolt(PVPositionerPC):
    readback = Cpt(EpicsSignalRO, 'Val:RB-E')
    setpoint = Cpt(EpicsSignal, 'Val:SP-E')
    stop_value = 1

#class VIMeterVirtualMotorOhm(PVPositionerPC):
#    readback = Cpt(EpicsSignalRO, 'Val:RB-R')
#    setpoint = Cpt(EpicsSignal, 'Val:RB-R')


class VIMeter(Device):
    curr = Cpt(VIMeterVirtualMotorCurr, '')
    volt = Cpt(VIMeterVirtualMotorVolt, '')
    ohm = Cpt(EpicsSignalRO, 'Val:RB-R')
    #ohm = Cpt(VIMeterVirtualMotorOhm, '')


# Vortex MCA

class Vortex(Device):
    mca = Cpt(EpicsMCA, 'mca1')
    vortex = Cpt(EpicsDXP, 'dxp1:')

    @property
    def trigger_signals(self):
        return [self.mca.erase_start]
