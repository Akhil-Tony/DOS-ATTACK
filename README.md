The one-slope model is a simplified path loss model used to estimate signal attenuation in wireless communication systems. It assumes a uniform loss rate over a given distance and does not account for specific environmental factors or variations in signal propagation.

In the one-slope model, the path loss is calculated using the following formula:

PL=PL0+10⋅n⋅log⁡10(d/d0)PL=PL0​+10⋅n⋅log10​(d/d0​)

Where:

    PLPL is the path loss in decibels (dB)
    PL0PL0​ is the reference path loss at a reference distance d0d0​ (usually 1 meter) in dB
    nn is the path loss exponent or slope of the decay (typically ranging from 2 to 4)
    dd is the distance between the transmitter and receiver

The one-slope model assumes that the path loss increases linearly with the logarithm of the distance. The path loss exponent (nn) represents the rate at which the signal strength decreases with distance. A higher nn value indicates a faster decay in signal strength over distance.


The dual-slope model is an extension of the one-slope model that takes into account the different path loss behaviors in the near-field and far-field regions of a wireless communication system. It provides a more accurate representation of signal attenuation by incorporating two different path loss exponents for different distance ranges.

In the dual-slope model, the path loss is calculated using the following formula:

PL=PL0+10⋅n1⋅log⁡10(d/d0)PL=PL0​+10⋅n1​⋅log10​(d/d0​) for d≤d1d≤d1​

PL=PL0+10⋅n1⋅log⁡10(d1/d0)+10⋅n2⋅log⁡10(d/d1)PL=PL0​+10⋅n1​⋅log10​(d1​/d0​)+10⋅n2​⋅log10​(d/d1​) for d>d1d>d1​

Where:

    PLPL is the path loss in decibels (dB)
    PL0PL0​ is the reference path loss at a reference distance d0d0​ (usually 1 meter) in dB
    n1n1​ is the path loss exponent for the near-field region
    n2n2​ is the path loss exponent for the far-field region
    dd is the distance between the transmitter and receiver
    d1d1​ is the threshold distance that separates the near-field and far-field regions

The dual-slope model recognizes that in the near-field region, path loss decreases at a faster rate due to the strong influence of near-field effects, such as electromagnetic coupling and reactive near-field components. As the distance increases and the system transitions into the far-field region, the path loss behavior follows a different slope.

The choice of d1d1​ and the values of n1n1​ and n2n2​ depend on the specific wireless environment and the characteristics of the system being modeled. These parameters are typically determined through empirical measurements or by using statistical models based on extensive data collection.



The model considers both line-of-sight (LOS) and non-line-of-sight (NLOS) scenarios, taking into account the effects of diffraction, reflection, and scattering. The original COST 231 Hata model was developed for the 900 MHz frequency band, but it has been extended to cover a broader frequency range.

The formula for path loss in the COST 231 Hata model is given as:

PL=PLurban+Ah+Af−13.82log⁡10(ht)−Cm+(44.9−6.55log⁡10(ht))log⁡10(d)PL=PLurban​+Ah​+Af​−13.82log10​(ht​)−Cm​+(44.9−6.55log10​(ht​))log10​(d)

Where:

    PLPL is the path loss in decibels (dB)
    PLurbanPLurban​ is the path loss in an urban environment at a reference distance and frequency
    AhAh​ is the correction factor for the height of the receiving antenna
    AfAf​ is the correction factor for the frequency
    htht​ is the height of the transmitting antenna in meters
    CmCm​ is the correction factor for the environment type (urban, suburban, or rural)
    dd is the distance between the transmitter and receiver in kilometers

The correction factors (AhAh​, AfAf​, CmCm​) are derived from empirical measurements and are based on the specific scenario being modeled. These factors help adjust the path loss estimate based on the characteristics of the antennas, frequency, and environment.
