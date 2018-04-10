#This code is written to simulate a pace calculator for triathalon as a sport with the functionality of individual sports.  what is needed?
# function for running
# function for swimming
# function for biking
# function for triathon(adding all together.)
# function for just adding any two

def calculator(pace=None,distance=None, time=None):
    #Helper function to perform the basic math.
    #pace is defined as  the running pace of the user over a distance . This can be calculated by dividing distance/time.
    # distance can be calculated by multiplying time * pace
    # time can be calculated  by distance/pace
    # pace=int(pace)
    # distance=int(distance)
    # time=int(time)
    if not pace :
        pace1 =int(time//distance)
        pace2=int(1/(time%distance)*60)
        pace=str(pace1)+':'+str(pace2)
        return pace
    elif not distance:
        distance = time/pace  #this conversion is for all unit of time converted to seconds.
        return distance
    elif not time:
        time=distance/pace
        return time

# def conversions():
#
# # 1 mile is 1609.34 meters
# # 1 kilometer is 1000 meters
# 1 meter is 1 meter
# 1 yard is 0.9144 meters
# 1 min is 60 seconds
# 1 hr is 3600 seconds
# 1 second is 1 second

# convert the given distance from the given units to meters
def to_meters(distance, units):
    if units == 'm':  # meters
        return distance
    elif units == 'mi': # miles
         distance * 1609.34
         round(distance,2)
         return distance
    elif units == 'km': # kilometers
        return distance * 1000
    elif units == 'yd': # yards
        return distance * 0.9144
    elif units == 'in': # inches
        return distance * 0.0254
# convert meters to the given distance unit
def from_meters(distance, units):
    if units == 'm':  # meters
        return distance
    elif units == 'mi': # miles
        return distance/1609.34
        round(distance,2)
        return distance
    elif units == 'km': # kilometers
        return distance / 1000
    elif units == 'yd': # yards
        return distance / 0.9144
    elif units == 'in': # inches
        return distance / 0.0254


# convert the given time from the given units to seconds
def to_seconds(time, units):
    if units == 's':  # seconds
        return time * 1
    elif units == 'min': # minutes
        return time * 60
    elif units == 'hr': # minutes
        return time * 3600

# convert from seconds to the given time unit.
def from_seconds(time, units):
        if units == 's':  # seconds
            return time
        elif units == 'min': # minutes
            return time/60
        elif units == 'hr': # minutes
            return time / 3600

def standardize_units(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['mi', 'mile', 'miles']:
        return 'miles'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['s', 'sec', 'second']:
        return 's'
    elif units in ['min', 'minute']:
        return 'min'
    elif units in ['h', 'hr', 'hrs','hours']:
            return 'h'


def run():
    rundecision=input("What do you want to do? calculate distance(d),pace(p) time(t):")

    if rundecision in ['distance', 'd']:

        while True:
            pacemin=input("Enter what pace you want to run/ you ran in :00(min):")#user pace in min
            pacesec=input("Enter what pace you want to run/ you ran in :00(secs):")#user pace in sec
            try:
                pacemin=int(pacemin)
                pacesec=int(pacesec)
                if  0 <= pacemin <= 59 and 0 <= pacesec <=59:
                    pacetotal=(to_seconds(pacemin,'min')) + (to_seconds(pacesec,'s'))
                    pacetotal=int(pacetotal)
                    break
            except :
                    print("your pace is entered incorrectly please enter in this format 00(min):00(secs) e.g 07:30:")


        while True:
            paceunit=input("Enter unit of your run pace mile, meter, yards or kilometer:")
            try:
                if paceunit in [ 'mile','mi','km','kilometer','y','yards','yard','meters','m']:
                    break
            except:
                print("your pace unit is entered incorrectly please enter any one of these units shown.  'mile','mi','km','kilometer','y','yards','yard','meters','m'")#exception to reengage user to enter the right units

        while True:
            timehr= input("Input your  hour(s) run time in 00(hr):")
            timemin=input("Input your minute(s) run time in 00(min):")
            timesec=input("Input your second(s) run time in 00(secs):")
            try:
                timehr=int(timehr)
                timemin=int(timemin)
                timesec=int(timesec)
                if 00 <= timehr <= 59 and 00 <= timemin <=59 and 00 <= timesec <=59:

                    timehr=to_seconds(timehr,'hr')#hrs converted to seconds

                    timemin=to_seconds(timemin,'min')#mins converted to seconds

                    timesec=to_seconds(timesec,'s')#seconds converted to seconds
                    timetotal=timehr+timemin+timesec
                    timetotal=int(timetotal)

                    break
            except:
                print("your time is entered incorrectly please enter in this format 00(hr):00(min):00(secs) e.g 1(hr):30(min):0(sec). Time must be an integer")
        distance=calculator(distance=None,pace=pacetotal,time=timetotal)
        return str(distance) + paceunit

    elif rundecision == 'pace' or 'p':
        distance=input("Enter what distance you will cover/covered in OO:")#user distance in ints
        while True:
                try:
                    distance=int(distance)
                    if  0 <= distance <= 999:

                        break
                except :
                    print("your distance needs to be an integer between 0-999")


        while True:
                distanceunit=input("Enter what distance unit you ran/will run   'mile','mi','km','kilometer','y','yards','yard','meters','m':")#user units

                try:
                    if distanceunit in ['mile','mi','km','kilometer','y','yards','yard','meters','m']:
                        break
                except :
                    print("your distance unit is entered incorrectly please enter any one of these units shown.  'mile','mi','km','kilometer','y','yards','yard','meters','m'")#exception to reengage user to enter the right units

        while True:
                timehr= input("Input your  hour(s) run time in 00(hr):")
                timemin=input("Input your minute(s) run time in 00(min):")
                timesec=input("Input your second(s) run time in 00(secs):")
                try:
                    timehr=float(timehr)
                    timemin=float(timemin)
                    timesec=float(timesec)
                    if 00 <= timehr <= 59 and 00 <= timemin <=59 and 00 <= timesec <=59:

                        timehr=to_seconds(timehr,'hr')#hrs converted to seconds

                        timemin=to_seconds(timemin,'min')#mins converted to seconds

                        timesec=to_seconds(timesec,'s')#seconds converted to seconds
                        timetotal=timehr+timemin+timesec



                        break
                except:
                    print("your time is entered incorrectly please enter in this format 00(hr):00(min):00(secs) e.g 1(hr):30(min):0(sec). Time must be an integer")

        timeoutput=input("Enter what time unit you want to calculate your pace in 'hr'(h),'min'(m),'sec'(s):")
        print("ringer")
        while True:
                try:
                    if timeoutput in ['hr','h','min','m','sec']:
                        timetotal=from_seconds(timetotal,timeoutput)

                        break
                except:
                    print("Please enter either of the units in the format below 'hr','h','min','m','sec'")

        pace=calculator(distance=distance,pace=None,time=timetotal)
        return str(pace)



print(run())
print(to_meters(10,standardize_units('miles')))
print(from_meters(1600, standardize_units('mile')))
print(to_seconds(30,'s'))
print(from_seconds(5400,'min'))
    # elif rundecision=='dp':
    #     timerun= input("Input your goal run time in 00(hr):00(mins):00(secs)")
    #     distancerun=input("Enter distance in miles(m) or kilometers(km):")
    #     distancerununit=input("Enter unit for your distance miles(m) or kilometers(km):")
    #     dp= float(distancerun/distancetime)
    #     return distancepace
    # elif rundecision=='dt':
    #     distancerun=input("Enter distance in :")
    #     distancerununit=input("Enter unit for your distance miles(m) or kilometers(km):")
    #     pacerun=input("Enter what pace you want to run/you ran:")
    #     pacerununit=input("Enter unit of your run pace min/mile or min/km:")
    #     dt=float(distancerun*pacerun)
    #     return dt
    # # else:
    #     break
# print(calc())





# distancerun=input("Enter distance in miles(m) or kilometers(km):")
# distancebike=input("Enter distance in miles(m) or kilometers(km):")
# distanceswim=input("Enter distance in yards(y), meters(m) or miles(mi):")
# pacerun=input("Enter what pace you want to run in min/mile:")
# pacebike=input("Enter what pace you want to ride in miles/hr:")
# paceswim=input("Enter what pace you want to swim in (y)/100m or (m)/100m:")
# timerun= input("Input your goal run time:")
# timebike=input("Enter your bike time:")
# timeswim=input("Enter your swim timerun")
# distancerun=distance.split("")
# distance=time*pace
# pace=distance/time
# time=distance/pace
