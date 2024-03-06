#XMLDefault
def xmldefault(serverIP, modelNumber, softwareVersion):
    x = open("XMLDefault.cnf.xml", "a")
    x.write("""<Default>
  <callManagerGroup>
    <members>
      <member priority="0">
        <callManager>
          <ports>
            <ethernetPhonePort>2000</ethernetPhonePort>
            <mgcpPorts>
              <listen>2427</listen>
              <keepAlive>2428</keepAlive>
            </mgcpPorts>
          </ports>
          <processNodeName>{}</processNodeName>
        </callManager>
      </member>
    </members>
  </callManagerGroup>
  <loadInformation model="Cisco {}">{}</loadInformation434>
  <authenticationURL></authenticationURL>
  <directoryURL></directoryURL>
  <idleURL></idleURL>
  <informationURL></informationURL>
  <messagesURL></messagesURL>
  <servicesURL></servicesURL>
</Default>""".format(serverIP, modelNumber, softwareVersion))
    x.close()
    print("XMLDefault.cnf.xml created!")

#PhoneConfig
def phoneConfig(macAddress, sshUser, sshPass, ntpServerIP, pbxIP, ext, extPass, ver):
    filename= ("SEP" + macAddress + ".cnf.xml")
    p = open(filename, "a")
    p.write("""<device>
    <deviceProtocol>SIP</deviceProtocol>
    <sshUserId>{}</sshUserId>
    <sshPassword>{}</sshPassword>
    <ipAddressMode>0</ipAddressMode>

    <devicePool>
        <dateTimeSetting>
            <dateTemplate>D/M/Ya</dateTemplate>
            <timeZone>Central Standard/Daylight Time</timeZone>
            <olsonTimeZone>US/Central</olsonTimeZone>
            <ntps>
                <ntp>
                    <name>{}</name>
                    <ntpMode>Unicast</ntpMode>
                </ntp>
            </ntps>
        </dateTimeSetting>

        <callManagerGroup>
            <members>
                <member priority="0">
                    <callManager>
                        <ports>
                            <ethernetPhonePort>2000</ethernetPhonePort>
                            <sipPort>5160</sipPort>
                        </ports>
                        <processNodeName>{}</processNodeName>
                    </callManager>
                </member>
            </members>
        </callManagerGroup>
    </devicePool>

    <sipProfile>
        <sipProxies>
            <registerWithProxy>true</registerWithProxy>
        </sipProxies>
        <sipCallFeatures>
            <cnfJoinEnabled>true</cnfJoinEnabled>
            <rfc2543Hold>false</rfc2543Hold>
            <callHoldRingback>2</callHoldRingback>
            <localCfwdEnable>true</localCfwdEnable>
            <semiAttendedTransfer>true</semiAttendedTransfer>
            <anonymousCallBlock>2</anonymousCallBlock>
            <callerIdBlocking>2</callerIdBlocking>
            <dndControl>0</dndControl>
            <remoteCcEnable>true</remoteCcEnable>
            <callForwardURI>x-serviceuri-cfwdall</callForwardURI>  
            <callPickupURI>x-cisco-serviceuri-pickup</callPickupURI>  
            <callPickupListURI>x-cisco-serviceuri-opickup</callPickupListURI>  
           <callPickupGroupURI>x-cisco-serviceuri-gpickup</callPickupGroupURI>  
           <meetMeServiceURI>x-cisco-serviceuri-meetme</meetMeServiceURI>  
           <abbreviatedDialURI>x-cisco-serviceuri-abbrdial</abbreviatedDialURI>  
        </sipCallFeatures>

        <sipStack>
            <sipInviteRetx>6</sipInviteRetx>
            <sipRetx>10</sipRetx>
            <timerInviteExpires>180</timerInviteExpires>
            <timerRegisterExpires>3600</timerRegisterExpires>
            <timerRegisterDelta>5</timerRegisterDelta>
            <timerKeepAliveExpires>120</timerKeepAliveExpires>
            <timerSubscribeExpires>120</timerSubscribeExpires>
            <timerSubscribeDelta>5</timerSubscribeDelta>
            <timerT1>500</timerT1>
            <timerT2>4000</timerT2>
            <maxRedirects>70</maxRedirects>
            <remotePartyID>true</remotePartyID>
            <userInfo>None</userInfo>
        </sipStack>

        <autoAnswerTimer>1</autoAnswerTimer>
        <autoAnswerAltBehavior>false</autoAnswerAltBehavior>
        <autoAnswerOverride>true</autoAnswerOverride>
        <transferOnhookEnabled>false</transferOnhookEnabled>
        <enableVad>false</enableVad>
        <preferredCodec>g711ulaw</preferredCodec>
        <dtmfAvtPayload>101</dtmfAvtPayload>
        <dtmfDbLevel>3</dtmfDbLevel>
        <dtmfOutofBand>avt</dtmfOutofBand>
        <alwaysUsePrimeLine>false</alwaysUsePrimeLine>
        <alwaysUsePrimeLineVoiceMail>false</alwaysUsePrimeLineVoiceMail>
        <kpml>3</kpml>
        <natEnabled>false</natEnabled>
        <phoneLabel>{}</phoneLabel>
        <stutterMsgWaiting>0</stutterMsgWaiting>
        <callStats>false</callStats>
        <silentPeriodBetweenCallWaitingBursts>10</silentPeriodBetweenCallWaitingBursts>
        <disableLocalSpeedDialConfig>false</disableLocalSpeedDialConfig>
        <startMediaPort>10000</startMediaPort>
        <stopMediaPort>20000</stopMediaPort>

        <sipLines>
            <line button="1">
                <featureID>9</featureID>
                <featureLabel>{}</featureLabel>
                <proxy>USECALLMANAGER</proxy>
                <port>5160</port>
                <name>{}</name>
                <displayName>{}</displayName>
                <autoAnswer>
                    <autoAnswerEnabled>2</autoAnswerEnabled>
                </autoAnswer>
                <callWaiting>3</callWaiting>
                <authName>{}</authName>
                <authPassword>{}</authPassword>
                <sharedLine>false</sharedLine>
                <messageWaitingLampPolicy>1</messageWaitingLampPolicy>
                <messagesNumber>*97</messagesNumber>
                <ringSettingIdle>4</ringSettingIdle>
                <ringSettingActive>5</ringSettingActive>
                <contact>{}</contact>
                <forwardCallInfoDisplay>
                    <callerName>true</callerName>
                    <callerNumber>true</callerNumber>
                    <redirectedNumber>false</redirectedNumber>
                    <dialedNumber>true</dialedNumber>
                </forwardCallInfoDisplay>
            </line>

        </sipLines>

        <voipControlPort>5160</voipControlPort>
        <dscpForAudio>184</dscpForAudio>
        <ringSettingBusyStationPolicy>0</ringSettingBusyStationPolicy>
        <dialTemplate>dialplan.xml</dialTemplate>
    </sipProfile>

    <commonProfile>
        <phonePassword></phonePassword>
        <backgroundImageAccess>true</backgroundImageAccess>
        <callLogBlfEnabled>1</callLogBlfEnabled>
    </commonProfile>

    <loadInformation>{}</loadInformation>
    <vendorConfig>
        <disableSpeaker>false</disableSpeaker>
        <disableSpeakerAndHeadset>false</disableSpeakerAndHeadset>
        <pcPort>0</pcPort>
        <settingsAccess>1</settingsAccess>
        <garp>0</garp>
        <voiceVlanAccess>0</voiceVlanAccess>
        <videoCapability>0</videoCapability>
        <autoSelectLineEnable>0</autoSelectLineEnable>
        <webAccess>0</webAccess>
        <spanToPCPort>1</spanToPCPort>
        <loggingDisplay>1</loggingDisplay>
        <loadServer></loadServer>
        <sshAccess>0</sshAccess>
        <sshPort>22</sshPort>
    </vendorConfig>

    <versionStamp>002</versionStamp>
    <networkLocale>United_Kingdom</networkLocale>
    <networkLocaleInfo>
        <name>United_Kingdom</name>
        <uid>64</uid>
        <version>1.0.0.0-4</version> 
    </networkLocaleInfo>

    <deviceSecurityMode>1</deviceSecurityMode>
    <authenticationURL></authenticationURL>  
    <servicesURL></servicesURL> 
    <directoryURL></directoryURL>  
    <idleURL></idleURL>  
    <informationURL></informationURL> 
    <messagesURL></messagesURL>  
    <proxyServerURL></proxyServerURL>  
    <dialToneSetting>2</dialToneSetting>
    <dscpForSCCPPhoneConfig>96</dscpForSCCPPhoneConfig>  
    <dscpForSCCPPhoneServices>0</dscpForSCCPPhoneServices>  
    <dscpForCm2Dvce>96</dscpForCm2Dvce>
    <capfAuthMode>0</capfAuthMode>  
    <capfList>  
      <capf>  
        <phonePort>3804</phonePort>  
      </capf>  
    </capfList> 
    <transportLayerProtocol>2</transportLayerProtocol>
    <certHash></certHash>  
    <encrConfig>false</encrConfig>  
</device>
""".format(sshUser, sshPass, ntpServerIP, pbxIP, ext, ext, ext, ext, ext, extPass, ext, ver))
    p.close()
    print(filename + " created!")

#Dialplan
def dialplan():
    d = open("dialplan.xml", "a")
    d.write("""<DIALTEMPLATE>
        <TEMPLATE MATCH="999" Timeout="0"/> <!-- Emergency -->
        <TEMPLATE MATCH="112" Timeout="0"/> <!-- Emergency -->
        <TEMPLATE MATCH="0500......" Timeout="0"/> <!-- Apparently 0500 is always 10 digits -->
        <TEMPLATE MATCH="0800......" Timeout="0"/> <!-- Apparently 0800 is always 10 digits -->
        <TEMPLATE MATCH="00*" Timeout="5"/> <!-- International, 00 prefixed. No fixed length -->
        <TEMPLATE MATCH="0.........." Timeout="0"/> <!-- UK 11 digit, 0 prefixed -->
        <TEMPLATE MATCH="26...." Timeout="0"/> <!-- My local STD numbers start 26 -->
        <TEMPLATE MATCH="\*.." Timeout="0"/> <!-- Asterisk *.. codes -->
        <TEMPLATE MATCH="\*98...." Timeout="0"/> <!-- Asterisk direct VM access *981234-->
        <TEMPLATE MATCH="1..." Timeout="0"/> <!-- Internal numbers -->
        <TEMPLATE MATCH="2..." Timeout="0"/>  <!-- Internal numbers -->
        <TEMPLATE MATCH="3..." Timeout="0"/>  <!-- Internal numbers -->
        <TEMPLATE MATCH="4..." Timeout="0"/>  <!-- Internal numbers -->
        <TEMPLATE MATCH="*" Timeout="5"/> <!-- Anything else -->
    </DIALTEMPLATE>""")
    d.close()
    print("dialplan.xml created!")