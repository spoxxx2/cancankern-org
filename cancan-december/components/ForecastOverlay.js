import React from 'react';

const ForecastOverlay = ({ objectData }) => {
  return (
    <div className="absolute inset-0 z-10 flex flex-col justify-end p-4 bg-black/40 backdrop-blur-[8px] transition-all duration-500 hover:backdrop-blur-none group">
      <div className="border-l-2 border-green-500 pl-3">
        <h3 className="text-white font-bold text-lg uppercase tracking-tighter">
          50-Year Forecast: {objectData.weathering_forecast_2076.appearance}
        </h3>
        <p className="text-green-400 text-xs font-mono">
          Integrity: {objectData.weathering_forecast_2076.structural_integrity} | Risk: {objectData.weathering_forecast_2076.danger_level}
        </p>
        <div className="mt-4 pt-2 border-t border-white/10">
          <span className="text-[10px] text-gray-400 uppercase">
            CANCAN (EIN: 39-2261270) | Adaptive Master Strategy
          </span>
        </div>
      </div>
    </div>
  );
};

export default ForecastOverlay;
