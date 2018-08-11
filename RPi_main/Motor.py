from abc import ABC, abstractmethod

class motor(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def clockwise(self, speed, checkMotor):
		pass
	
	@abstractmethod
	def counterClockwise(self, speed, checkMotor):
		pass
	
	@abstractmethod
	def stop():
		pass

class L293d(motor):
	def __init__(self, pinE, pinA, pinB):
		self._pinE = pinE
		self._pinA = pinA
		self._pinB = pinB
		
		GPIO.setup(pinE, GPIO.OUT)
		GPIO.setup(pinA, GPIO.OUT)
		GPIO.setup(pinB, GPIO.OUT)

		self._pwmE = GPIO.PWM(pinE, 100)
		self._pwmE.start(0)

	def clockwise(self, speed):
		GPIO.output(pinE, True)
		GPIO.output(pinA, True)
		GPIO.output(pinB, False)
		self._pwmE.ChangeDutyCycle(speed)

	def counterCLockwise(self, speed):
		GPIO.output(pinE, True)
		GPIO.output(pinA, False)
		GPIO.output(pinB, True)
		self._pwmE.ChangeDutyCycle(speed)

	def stop():
		GPIO.output(pinE, False)
		GPIO.output(pinA, False)
		GPIO.output(pinB, False)
		self._pwmE.ChangeDutyCycle(0)

class driver(motor):
	def __init__(self):
		self._R_EN = R_EN
		self._L_EN = L_EN
		self._RPWM = RPWM
		self._LPWM = LPWM

		GPIO.setup(R_EN, GPIO.OUT)
		GPIO.setup(L_EN, GPIO.OUT)
		GPIO.setup(RPWM, GPIO.OUT)
		GPIO.setup(LPWM, GPIO.OUT)

		self._pwmR = GPIO.PWM(RPWM, 100)
		self._pwmL = GPIO.PWM(LPWM, 100)
		self._pwmR.start(0)
		self._pwmL.start(0)

	def clockwise(self, speed):
		GPIO.output(self._R_EN, True)
		GPIO.output(self._L_EN, True)
		self._pwmR.ChangeDutyCycle(speed)
		self._pwmL.ChangeDutyCycle(0)

	def counterCLockwise(self, speed):
		GPIO.output(self._R_EN, True)
		GPIO.output(self._L_EN, True)	
		self._pwmR.ChangeDutyCycle(0)
		self._pwmL.ChangeDutyCycle(speed)

	def stop():
		GPIO.output(self._R_EN, False)
		GPIO.output(self._L_EN, False)
		self._pwmR.ChangeDutyCycle(0)
		self._pwmL.ChangeDutyCycle(0)