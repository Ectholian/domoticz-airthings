"""
<plugin key="airthings" name="Airthings" author="ectholian" version="1.0.0" wikilink="http://www.domoticz.com/wiki/plugins/Kodi.html" externallink="https://www.airthings.com">
    <description>
        <h2>Airthings Plugin</h2><br/>
        <h3>Features</h3>
        <ul style="list-style-type:square">
            <li>Polls Airthings API periodically</li>
            <li>Support for wave, wave mini, wave plus, wave radon, view plus, view pollution and view radon</li>
        </ul>
        <h3>Devices</h3>
        <h4>Dependent on device type</h4>
        <ul style="list-style-type:square">
            <li>CO2 - Basic status indicator, On/Off. Also has icon for Kodi Remote popup</li>
            <li>Humidity - Icon mutes/unmutes, slider shows/sets volume</li>
            <li>Mold - Selector switch for content source: Video, Music, TV Shows, Live TV, Photos, Weather</li>
            <li>PM25 - Icon Pauses/Resumes, slider shows/sets percentage through media</li>
            <li>Pressure</li>
            <li>Radon</li>
            <li>Temperature</li>
            <li>VOC</li>
        </ul>
    </description>
    <params>
        <param field="username" label="Client ID" width="200px" required="true"/>
        <param field="password" label="Secret" width="200px" required="true" password="true"/>
        <param field="Mode1" label="Refresh Interval (s)" width="30px" required="true" default="360"/>
        <param field="Mode2" label="Device Type" width="200px" required="true">
            <options>
                <option label="Wave" value="wave"/>
                <option label="Wave Mini" value="wave-mini"/>
                <option label="Wave Plus" value="wave-plus"/>
                <option label="Wave Radon" value="wave-radon"/>
                <option label="View Plus" value="view-plus"/>
                <option label="View Pollution" value="view-pollution"/>
                <option label="View Radon" value="view-radon"/>
                <option label="Other" value="other" />
            </options>
        </param>
        <param field="Mode6" label="Debug" width="75px">
            <description><h2>Debugging</h2>Enable to see debug logging</description>
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>
"""
