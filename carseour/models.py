import carseour.definitions

class GameInstance(carseour.definitions.GameInstance):
    def wheels(self):
        wheels = []

        for i in range(0, carseour.definitions.TYRE_MAX):
            wheels.append({
                'tyre': {
                    'flags': self.mTyreFlags[i],
                    'y': self.mTyreY[i],
                    'rps': self.mTyreRPS[i],
                    'slip_speed': self.mTyreSlipSpeed[i],
                    'temp': self.mTyreTemp[i],
                    'grip': self.mTyreGrip[i],
                    'height_above_ground': self.mTyreHeightAboveGround[i],
                    'lateral_stiffness': self.mTyreLateralStiffness[i],
                    'wear': self.mTyreWear[i],
                    'thread_temp': self.mTyreTreadTemp[i],
                    'layer_temp': self.mTyreLayerTemp[i],
                    'carcass_temp': self.mTyreCarcassTemp[i],
                    'rim_temp': self.mTyreRimTemp[i],
                    'internal_air_temp': self.mTyreInternalAirTemp[i],
                },
                'suspension': {
                    'damage': self.mSuspensionDamage[i],
                },
                'brakes': {
                    'damage': self.mBrakeDamage[i],
                    'temp_celcius': self.mBrakeTempCelsius[i],
                },
                'terrain': {
                    'lookup_value': self.mTerrain[i],
                },
            })

        return wheels

    def players(self):
        players = []

        for participant in self.mParticipantInfo:
            if len(participant.mName) > 0:
                players.append(participant)

        return players

    def standing(self):
        standing = []

        for player in self.players():
            standing.append({
                'name': player.mName.decode("iso-8859-1"),
                'position': player.mRacePosition,
                'lap': player.mCurrentLap,
                'lap_distance': player.mCurrentLapDistance,
                'laps_completed': player.mLapsCompleted,
            })

        standing = sorted(standing, key=lambda player: player['position'])

        return standing
