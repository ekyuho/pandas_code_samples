#include <OneWire.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS D4


String url = "http://api.thingspeak.com/update?api_key=QIXPNVA5JX89WDTX&field1=";

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature DS18B20(&oneWire);

void setup(void){
	Serial.begin(115200);
	Serial.print("\n\nBegin ");

	WiFi.begin("cookie2", "0317137263");
	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print(".");
	}

	Serial.printf("\nGot connected. IP address= ");
	Serial.println(WiFi.localIP());

	DS18B20.begin();
}

void loop() {
	DS18B20.requestTemperatures(); 
	float temperature = DS18B20.getTempCByIndex(0);
	Serial.printf("\ntemperature=%f ", temperature);

	WiFiClient client;
	HTTPClient http;

	http.begin(client, url+String(temperature));
	int r = http.GET();
	Serial.printf("got r=%d, %s", r, http.getString().c_str());

	http.end();
	delay(15000);
}
