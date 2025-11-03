defmodule Lasagna do
  def expected_minutes_in_oven() do
    40
  end

  def remaining_minutes_in_oven(minutes_in_oven) do
    expected_minutes_in_oven() - minutes_in_oven
  end

  def preparation_time_in_minutes(num_layers_added) do
    num_layers_added * 2
  end

  def total_time_in_minutes(num_layers_added, minutes_in_oven) do
    preparation_time_in_minutes(num_layers_added) + minutes_in_oven
  end

  def alarm(), do: "Ding!"
end
