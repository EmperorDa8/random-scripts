# to write text using action action into google docs

from selenium.webdriver import Chrome,Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

url="https://docs.google.com/document/d/1WgCbokU0IJEo9BJWDW_TwuVFjG-X_w8ys3BdWnDnOMo/edit"
driverpath="Downloads//chromedriver.exe"

texts='''A mishap was averted at the airside of the Murtala Muhammed Airport, Lagos when a speeding vehicle had a near collision with a Dana Air plane taxiing to take off on Runway 18L of the airport.

The unfortunate incident, which happened on December 21, 2021, occurred barely one week after a landing Max Air jet almost rammed into a malfunctioning car being tested on Runway 18L.

However, the latest incident involved a Dana Air MD 83 plane with registration number 5N JOY which was departing Lagos airport for Enugu with a total of 157 passengers and seven crew members on board.

The aircraft was taxiing to join Runway 18L for take-off when the speeding car almost rammed into it.

A taxiway is a path for aircraft that connects a runway with another area of an airport.

Sources close to the incident said the vehicle, reportedly belonging to the Nigeria Customs Service, was being driven by one of its officers when the incident occurred.

The angry pilot was said to have immediately called the Lagos airport control tower to report the incident.

NAMA officials at the control tower subsequently alerted FAAN’s airside personnel who swiftly went after the driver.

A FAAN source close to the incident said, “The pilot of Dana Air flight 0371 complained angrily about a military vehicle that drove dangerously past his nose, forcing him to apply brakes suddenly. The NAMA officials in the control tower sighted the vehicle and instructed FAAN airside personnel to apprehend the team immediately.

“The vehicle was apprehended by MM123. It was reported to the control tower that it was a Customs vehicle. They were immediately taken to AVSEC for further questioning. The Dana plane was later airborne at 11:27am. The name of the Customs driver who was apprehended by MM123 is Wilfed .T. with ODC number 36789.”

Officials of the Nigerian Airspace Management Agency and the Federal Airports Authority of Nigeria confirmed the incident on condition of anonymity because they were not authorised to speak on the matter.

Also, the General Manager, Public Affairs, FAAN, Mrs Henrieta Yakubu, confirmed the development but said the agency had since improved security at the airside of the airport after the incident.

“We have reinforced security on the airside,” she said. She did not give further details.

However, FAAN officials suspected the driver was not probably trained in airside driving.

“Other agencies deploy new officers to the airport from time to time but I am not sure if FAAN ensures these officers are trained in airside driving. I suspect this driver was not properly trained in airside driving. It is unlikely someone trained in airside driving will behave in such a very dangerous manner,”’ a FAAN official said on condition of anonymity.

FAAN had suspended some officials after the Max Air incident. Our correspondent could not confirm if a similar action was taken after the latest incident but officials said the agency needed to take steps to strengthen airside security at the flagship airport.

FAAN had been involved in some major runway and airside incursion incidents in the past.

There was pandemonium at the airside of the Lagos airport on December 27, 2019 as an unidentified man found his way into the airside mysteriously and mounted a moving Air Peace plane.

The man was later arrested by security operatives who were notified by the pilot of a private jet coming behind the Air Peace plane.

The incident happened barely six months after a man found his way into the Lagos airport and climbed a Port Harcourt-bound Azman Airlines plane.

The man, believed to be mentally ill, was later identified as Usman Adamu from the Republic of Niger.

The Police said the Nigerien could not speak or understand English Language.

The authorities said then that investigation was still ongoing to ascertain how Adamu gained access to the restricted area at the airport.

According to a video clip by one of the Port Harcourt-bound passengers, Adamu was seen entering the fuselage of the aircraft with hand luggage and also climbing one of its wings.

He was later apprehended by Aviation Security Personnel of FAAN and taken to its detention facility before the case was transferred to the Police for further investigation.
'''


xpath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
spath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"

browser=Chrome(executable_path=driverpath)
browser.get(url)


actionp=ActionChains(browser)
actionp.send_keys("Uabdul88@gmail.com").perform()

browser.find_element_by_xpath(spath).click()



#action=ActionChains(browser)
#action.send_keys(texts).perform()