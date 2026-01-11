import React from 'react';

const ForecastOverlay = ({ objectData }) => {
  return (
    <div className="absolute inset-0 z-10 flex flex-col justify-end p-6 bg-black/60 backdrop-blur-[8px] transition-all duration-700 hover:backdrop-blur-none group">
      <div className="border-l-4 border-green-500 pl-4 bg-black/20 p-2">
        <h3 className="text-white font-bold text-xl uppercase tracking-tighter mb-1">
          2076 FORECAST: {objectData.weathering_forecast_2076?.appearance || "CALIBRATING..."}
        </h3>
        <p className="text-green-400 text-xs font-mono mb-4">
          STRUCTURAL INTEGRITY: {objectData.weathering_forecast_2076?.structural_integrity} | RISK: {objectData.weathering_forecast_2076?.danger_level}
        </p>
        <div className="pt-2 border-t border-white/20">
          <p className="text-[9px] text-gray-500 font-mono">
            CANCAN (EIN: 39-2261270) | ADAPTIVE MASTER STRATEGY | SPECTRAL_ID: {objectData.sub_type}
          </p>
        </div>
      </div>
    </div>
  );
};

export default ForecastOverlay;
