class LightSwitch():
    ''' A class to represent a light and we can turn on and turn off
    the light.'''

    def __init__(self):
        ''' (LightSwitch) -> NoneType
        Create a light and it is off.
        '''
        # let light begin at off
        self._light = 'off'

    def state(self):
        ''' (LgihtSwitch) -> str
        Return the status of the light, the result should be either on or off.
        '''
        return self._light == 'on'

    def turn_on(self):
        ''' (LightSwitch) -> NoneType
        The function will only return on the light.
        If the light is on, then do nothing.
        '''
        self._light = 'on'

    def turn_off(self):
        ''' (LightSwitch) -> NoneType
        The function will only return off the light.
        If the light is off, then do nothing.
        '''
        self._light = 'off'

    def flip(self):
        ''' (LightSwitch) -> NoneType
        The function will flip the light.
        If the light is on, then turn it off.
        If the light is off, then turn it on.
        '''
        # if light is on, then turn it off
        if self._light == 'on':
            self.turn_off()
        # if light is off, then turn it on
        elif self._light == 'off':
            self.turn_on()

    def __str__(self):
        ''' (LightSwitch) -> str
        Return a string represent this light.
        '''
        result = 'I am ' + self._light
        return result


class SwitchBoard():
    ''' A class represent a switch board of lights, we can flip any lights
    if they are on the switch board.'''

    def __init__(self, num_lights):
        ''' (SwitchBoard, int) -> NoneType
        Create a switchboard and the number of switches on it is based on
        num_lights.
        '''
        # initialize lights as a list
        self._lights = []
        # get the vaue of lights
        self._num_lights = num_lights
        # loop through each light
        for i in range(self._num_lights):
            # for each light get an object and add into list
            self._light = LightSwitch()
            self._lights.append(self._light)

    def __str__(self):
        ''' (SwitchBoard) -> str
        The function will return a string that show the following switches.
        '''
        result = 'The following switches are'
        result_list = self.which_switch()
        for switch in result_list:
            result = result + ' ' + str(switch)
        return result

    def which_switch(self):
        ''' (SwitchBoard) -> list of int
        The function will determine which lights are still on, and add
        the number of these lights into the result list, and finally
        return this result list.
        '''
        # initialize index and result
        index = 0
        result = []
        # loop through each light to check if it is on
        while index < len(self._lights):
            if self._lights[index].state():
                # if light is on then add into result
                result.append(index)
            index += 1
        return result

    def flip(self, num):
        ''' (SwitchBoard, int) -> NoneType
        The function will flip a particular light and
        it is based on the input variable num.
        '''
        # flip specific light by calling method from LgithSwitch
        self._lights[num].flip()

    def flip_every(self, num):
        ''' (SwitchBoard, int) -> NoneType
        The function will flip the states of every n'th lightswitch,
        starting at 0.
        The number n is based on the parameter num.

        REQ: num != 0
        '''
        # initialize index
        index = 0
        # loop through each light to check if it is divisble by num,
        # if num is too big or num == 0, then do nothing,
        # to make sure the function will not crash
        while((index < len(self._lights)) and (num < len(self._lights)) and
              (num != 0)):
            if index % num == 0:
                # if the light is divisible by num, then flip it
                self.flip(index)
            index += 1

    def reset(self):
        ''' (SwitchBoard) -> NoneType
        The funcion will reset all the lights which means turn off all
        the lights by calling __init__().
        '''
        # reset all the lights
        self.__init__(self._num_lights)


def test():
    ''' This function is only used for testing'''
    lights = SwitchBoard(1024)
    for i in range(1024):
        lights.flip_every(i)
    print(lights)


if __name__ == '__main__':
    test()
